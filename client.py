import grpc
from concurrent import futures
import time

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc


# open a gRPC channel
channel = grpc.insecure_channel("localhost:50051")


# create a valid request message
number = calculator_pb2.Number(value=1000)


stub = calculator_pb2_grpc.CalculatorStub(channel)


# make the call
response = stub.SquareRoot(number)

# get the result
print(f'Result: {response.value}')

