from flask import Flask, jsonify, request

import tensorflow as tf
import numpy as np
import os

import tensorflow.keras as keras
from tensorflow.keras.preprocessing.image import array_to_img

from flask import send_file
import io
import zipfile

app = Flask(__name__)

# Pricing
prices = [
    {'id': 1, 'title': '1 fingerprint', 'price': '0.0001$'},
    {'id': 2, 'title': '10 fingerprints', 'price': '0.001$'},
]

# Get all task prices
@app.route('/pricing', methods=['GET'])
def get_pricing():
    return jsonify(prices)

@app.route('/generate_one', methods=['GET'])
def generate_one():
    zip_content = generate_images(1)

    return send_file(
        io.BytesIO(zip_content),
        as_attachment=True,
        download_name='generated_image.zip'
    )

@app.route('/generate_ten', methods=['GET'])
def generate_ten():
    zip_content = generate_images(10)

    return send_file(
        io.BytesIO(zip_content),
        as_attachment=True,
        download_name='generated_images.zip'
    )

# Generate image
def generate_images(images):
    generator = keras.models.load_model('generator_main.h5')

    generated_images = generator.predict(tf.random.normal((int(images), 16, 1)))
    generated_images *= 255

    # Create an in-memory zip file
    zip_file = io.BytesIO()

    # Create a zip file object
    with zipfile.ZipFile(zip_file, 'w') as zipf:
        # Save the generated images as PNG files and add them to the zip file
        for i in range(int(images)):
            img = array_to_img(generated_images[i])
            img_file = io.BytesIO()
            img.save(img_file, format='PNG')
            zipf.writestr(f'fingerprint_{i+1}.png', img_file.getvalue())

    # Get the content of the zip file as bytes
    zip_content = zip_file.getvalue()

    return zip_content


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
