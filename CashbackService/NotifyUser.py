import time
from concurrent import futures
from kafka import KafkaConsumer, errors
from json import loads
import grpc
import Protos.notify_pb2
import Protos.notify_pb2_grpc
import Handler.notify_handler
import logging


def notify(consumer):
    while True:
        for message in consumer:
            message = message.value
            print(message)
            time.sleep(1)
            if Handler.notify_handler.check_user_exists(message['user']) is None:
                Handler.notify_handler.insert(message['user'])
                time.sleep(1)
            else:
                Handler.notify_handler.update(message['user'])
                time.sleep(1)
            consumer.commit()


def serve():
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Protos.notify_pb2_grpc.add_cashBackApiServicer_to_server(CashBackService(), grpc_server)
    grpc_server.add_insecure_port('[::]:9999')
    grpc_server.start()
    ready_consumer()
    while True:
        time.sleep(860000)


def ready_consumer():
    consumer = None
    while consumer is None:
        try:
            consumer = KafkaConsumer(
                'notify',
                bootstrap_servers=['localhost:9092'],  # kafka|localhost
                auto_offset_reset='earliest',
                enable_auto_commit=True,
                group_id='notifiers',
                value_deserializer=lambda x: loads(x.decode('utf-8')))
        except errors.NoBrokersAvailable:
            logging.debug("No Broker")
            time.sleep(1)
    notify(consumer)


class CashBackService(Protos.notify_pb2_grpc.cashBackApiServicer):
    def sendMessage(self, request, context):
        if Handler.notify_handler.get_count(request.userId) % 5 == 0:
            Handler.notify_handler.reset(request.userId)
            return Protos.notify_pb2.message(
                eligible=True,
                Msg='You are eligible for a cash back')
        return Protos.notify_pb2.message(
            eligible=False,
            Msg='You are eligible for a cash back')


if __name__ == '__main__':
    serve()
