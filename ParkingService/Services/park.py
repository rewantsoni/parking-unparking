import grpc
import Protos.user_parking_pb2 as user_parking_pb2
import Protos.user_parking_pb2_grpc as user_parking_pb2_grpc
import Protos.parking_pb2
import Protos.parking_pb2_grpc
from concurrent import futures
import time
import Handler.parking_handler as parking_handler
import re
from kafka import KafkaProducer, errors
from json import dumps
from time import sleep
import pybreaker
LOCATION = 4
SLOT = 4
FLOOR = 10
ONE_DAY = 860000
REGEX_FOR_LOCATION = r'^L[0-3]S[0-3]F(([1][0])|[0-9])$'
circuit_breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=10)
loc = [0 for i in range(LOCATION * SLOT * FLOOR)]


@circuit_breaker
def is_user_valid(user, context):
    channel = grpc.insecure_channel('192.168.99.101:30100')
    client = user_parking_pb2_grpc.userParkingApiStub(channel)
    # try:
    return client.validate_user(user_parking_pb2.user(user=user)).msg
    # except grpc.RpcError:
    #     context.set_code(grpc.StatusCode.UNAVAILABLE)
    #     context.set_details('User service is not available')
    #     raise grpc.RpcError


def serve():
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Protos.parking_pb2_grpc.add_userApiServicer_to_server(ParkUnParkService(), grpc_server)
    grpc_server.add_insecure_port('localhost:8888')
    grpc_server.start()
    print('Server Started')
    while True:
        time.sleep(ONE_DAY)


def get_empty_parking_space(context):
    try:
        return loc.index(0)
    except ValueError:
        context.set_code(grpc.StatusCode.UNAVAILABLE)
        context.set_details('No parking Space is available')
        raise grpc.RpcError


def check_position(position):
    return re.match(REGEX_FOR_LOCATION, position, flags=0)


def get_location(location):
    return int(int(location[1:2]) * SLOT * FLOOR + int(location[3:4]) * FLOOR + int(location[5:]))


def return_error(context, error_code, error_details):
    context.set_code(error_code)
    context.set_details(error_details)
    raise grpc.RpcError


class ParkUnParkService(Protos.parking_pb2_grpc.userApiServicer):

    def park(self, request, context):
        print('responded')
        try:
            producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                     value_serializer=lambda x:
                                     dumps(x).encode('utf-8'))
        except errors.NoBrokersAvailable:
            context.set_code(grpc.StatusCode.ABORTED)
            context.set_details('Kafka Broker not available')
            raise errors.NoBrokersAvailable
        if not is_user_valid(request.userId, context):
            return_error(context, grpc.StatusCode.INVALID_ARGUMENT, 'User Id is not valid')
        print('user is valid')
        parking_location = get_empty_parking_space(context)
        print('checking for a response')
        response = parking_handler.parking(request, parking_location)
        print('got a response')
        if response is None:
            return_error(context, grpc.StatusCode.ALREADY_EXISTS, 'Car already in Parking')
        loc[parking_location] = 1
        data = {'user': request.userId}
        producer.send('notify', value=data)
        sleep(1)
        print("{}".format(response))
        return Protos.parking_pb2.location(location=response)

    def unPark(self, request, context):
        """for unParking"""
        if not is_user_valid(request.userId, context):
            return_error(context, grpc.StatusCode.INVALID_ARGUMENT, 'User Id is not valid')
        if check_position(request.location.location) is None:
            return_error(context, grpc.StatusCode.INVALID_ARGUMENT, 'Invalid Location')
        res = parking_handler.un_parking(request, context)
        location = get_location(request.location.location)
        loc[location] = 0
        return Protos.parking_pb2.response(Msg=res)
