import grpc
import time
import Protos.admin_parking_pb2
import Protos.admin_parking_pb2_grpc
import Handler.admin_parking_handler as admin_parking_handler
from concurrent import futures


def serve():
    admin_parking_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Protos.admin_parking_pb2_grpc.add_adminParkingApiServicer_to_server(AdminParkingService(), admin_parking_server)
    admin_parking_server.add_insecure_port('localhost:31743')
    admin_parking_server.start()
    while True:
        time.sleep(860000)


class AdminParkingService(Protos.admin_parking_pb2_grpc.adminParkingApiServicer):
    def insert(self, request, context):
        admin_parking_handler.insert(request)
        return Protos.admin_parking_pb2.stub()

    def update(self, request, context):
        admin_parking_handler.update(request)
        return Protos.admin_parking_pb2.stub()
