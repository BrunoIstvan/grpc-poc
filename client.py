import grpc
import sys

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

args = len(sys.argv)

# open a gRPC channel
channel = grpc.insecure_channel("localhost:50051")
stub = calculator_pb2_grpc.CalculatorStub(channel)

for i in range(1, args):
    n = int(sys.argv[i])

    # create a valid request message
    number = calculator_pb2.Number(value=n)

    # make the call
    response = stub.SquareRoot(number)

    # get the result
    print(f'Square Root of {n} is {response.value}')

