from Handler.user_handler import get_users
import grpc
import time
import Protos.user_parking_pb2
import Protos.user_parking_pb2_grpc
from concurrent import futures


def serve():
    user_parking_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Protos.user_parking_pb2_grpc.add_userParkingApiServicer_to_server(UserParkingService(), user_parking_server)
    user_parking_server.add_insecure_port('[::]:30100')
    user_parking_server.start()
    print('started')
    while True:
        time.sleep(860000)


class UserParkingService(Protos.user_parking_pb2_grpc.userParkingApiServicer):
    def validate_user(self, request, context):
        if request.user in get_users():
            return Protos.user_parking_pb2.message(msg=True)
        return Protos.user_parking_pb2.message(msg=False)
