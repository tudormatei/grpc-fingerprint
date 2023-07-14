from concurrent import futures
import grpc
import fingerprint_pb2
import fingerprint_pb2_grpc

import tensorflow.keras as keras
import tensorflow as tf

import numpy as np
import io
from PIL import Image

class FingerprinterServicer(fingerprint_pb2_grpc.FingerprinterServicer):
    def GenerateOne(self, request, context):
        print(f'Generate one fingerprint request made from token: {request.token}')

        generator = keras.models.load_model('generator_main.h5')

        images = 1
        generated_images = generator.predict(tf.random.normal((int(images), 16, 1)))
        generated_images *= 255
        
        img = np.squeeze(generated_images)

        # Convert the 3D array to a PIL Image object
        img = Image.fromarray(img.astype(np.uint8))

        # Create a BytesIO object to hold the byte stream
        byte_stream = io.BytesIO()

        img.save(byte_stream, format='JPEG')

        # Get the byte string value from the BytesIO object
        byte_string = byte_stream.getvalue()

        # Create a Fingerprint message with the image data
        fingerprint = fingerprint_pb2.Fingerprint(image_data=byte_string)

        return fingerprint

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    fingerprint_pb2_grpc.add_FingerprinterServicer_to_server(FingerprinterServicer(), server)
    server.add_insecure_port('0.0.0.0:8080')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

