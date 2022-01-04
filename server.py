import grpc
from concurrent import futures
import time

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# import the original calculator.py
import calculator


class CalculatorService(calculator_pb2_grpc.CalculatorServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type calculator_pb2.Number
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        print('Request value: ', request.value)
        response.value = calculator.square_root(request.value)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server` to add the defined class to the server
calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorService(), server)

# Listen on port 50051
print('Starting server! Listening on port 50051.')
server.add_insecure_port("[::]:50051")
server.start()

# since server.start() whill be not block, a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
