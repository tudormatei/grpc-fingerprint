FROM python:3.9
RUN pip install grpcio grpcio-tools
RUN pip install Pillow
RUN pip install tensorflow==2.10.1
RUN pip install protobuf==3.20.0
ADD fingerprint_server.py /
ADD fingerprint_pb2_grpc.py /
ADD fingerprint_pb2.py /
EXPOSE 8080
CMD [ "python", "./fingerprint_server.py"]
