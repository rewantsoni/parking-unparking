import datetime
import re
from Handler.admin_handler import get_admins
import grpc
import time
import Protos.admin_parking_pb2
import Protos.admin_parking_pb2_grpc
import Handler.admin_parking_handler as admin_parking_handler
import Protos.admin_pb2
import Protos.admin_pb2_grpc
from concurrent import futures
import pybreaker

circuit_breaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=15)
REGEX_FOR_LOCATION = r'^L[0-3]S[0-3]F(([1][0])|[0-9])$'


def serve():
    admin_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Protos.admin_pb2_grpc.add_adminApiServicer_to_server(AdminService(), admin_server)
    admin_server.add_insecure_port('[::]:8083')
    admin_server.start()

    while True:
        time.sleep(860000)


@circuit_breaker
def validate_admin(admin):
    if admin in get_admins():
        return admin
    return False


def validate_date(date):
    return datetime.datetime.strptime(date, '%Y-%m-%d')


def validate_location(position):
    return re.match(REGEX_FOR_LOCATION, position, flags=0)


def mapping(cars):
    mylist = Protos.admin_pb2.Parkings()
    print(cars)
    for car in cars:
        if car.date_out is None:
            mylist.Parkings.append(Protos.admin_pb2.Parking(
                parking_id=car.parking_id, user_id=car.user_id,
                car_id=car.car_id,
                date_in=car.date_in.strftime("%m/%d/%Y, %H:%M:%S"),
                date_out='', location=car.location,
                isparked=car.isparked, ))
            continue
        mylist.Parkings.append(Protos.admin_pb2.Parking(
            parking_id=car.parking_id, user_id=car.user_id,
            car_id=car.car_id,
            date_in=car.date_in.strftime("%m/%d/%Y, %H:%M:%S"),
            date_out=car.date_out.strftime("%m/%d/%Y, %H:%M:%S"),
            location=car.location, isparked=car.isparked, ))
    return mylist


def return_error(context, error_code, error_details):
    context.set_code(error_code)
    context.set_details(error_details)
    raise grpc.RpcError


class AdminService(Protos.admin_pb2_grpc.adminApiServicer):
    def getAllCar(self, request, context):
        if validate_admin(request.adminId) is False:
            return_error(context, grpc.StatusCode.PERMISSION_DENIED, 'Not the admin Id we expected')
        return mapping(admin_parking_handler.get_all(context))

    def getAllCarParked(self, request, context):
        if validate_admin(request.adminId) is False:
            return_error(context, grpc.StatusCode.PERMISSION_DENIED, 'Not the admin Id we expected')
        return mapping(admin_parking_handler.get_all_parked(context))

    def getAllCarParkedByDate(self, request, context):
        if validate_admin(request.admin.adminId) is False:
            return_error(context, grpc.StatusCode.PERMISSION_DENIED, 'Not the admin Id we expected')
        if validate_date(request.date) is None:
            return_error(context, grpc.StatusCode.INVALID_ARGUMENT, 'Invalid date Entered')
        return mapping(admin_parking_handler.get_all_car_parked_by_date(context, validate_date(request.date)))

    def getAllCarByLocation(self, request, context):
        if validate_admin(request.admin.adminId) is False:
            return_error(context, grpc.StatusCode.PERMISSION_DENIED, 'Not the admin Id we expected')
        if validate_location(request.location.location) is None:
            return_error(context, grpc.StatusCode.INVALID_ARGUMENT, 'Invalid Location format')
        return mapping(admin_parking_handler.get_all_car_by_location(request.location.location, context))

    def getCarParkingDetails(self, request, context):
        if validate_admin(request.admin.adminId) is False:
            return_error(context, grpc.StatusCode.PERMISSION_DENIED, 'Not the admin Id we expected')
        return mapping(admin_parking_handler.get_car_parking_details(request.carId.carId, context))

    def getCarByLocationCurrentlyParked(self, request, context):
        if validate_admin(request.admin.adminId) is False:
            return_error(context, grpc.StatusCode.PERMISSION_DENIED, 'Not the admin Id we expected')
        if validate_location(request.location.location) is None:
            return_error(context, grpc.StatusCode.INVALID_ARGUMENT, 'Invalid Location format')
        return mapping(admin_parking_handler.get_car_by_location_currently_parked(request.location.location, context))

    def getCarByLocationCarId(self, request, context):
        if validate_admin(request.admin.adminId) is False:
            return_error(context, grpc.StatusCode.PERMISSION_DENIED, 'Not the admin Id we expected')
        if validate_location(request.location.location) is None:
            return_error(context, grpc.StatusCode.INVALID_ARGUMENT, 'Invalid Location format')
        admin_parking_handler.get_car_by_location_car_id(request, context)
        return Protos.admin_pb2.message(msg='Car found at the location')
