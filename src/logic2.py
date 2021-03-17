import io
import os
from dataclasses import dataclass 

@dataclass
class Photo: 
    src: str
    path: str

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
vision_client = vision.ImageAnnotatorClient()

german_1 = Photo(src="local", path="../photos/german1.jpeg")
german_2 = Photo(src="local", path="../photos/german2.png")


# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    german_2.path)

client = vision.ImageAnnotatorClient()

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations

print(texts)

print('Texts:')


for text in texts:
    print('\n"{}"'.format(text.description))

    vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in text.bounding_poly.vertices])

    print('bounds: {}'.format(','.join(vertices)))

if response.error.message:
    raise Exception(
        '{}\nFor more info on error messages, check: '
        'https://cloud.google.com/apis/design/errors'.format(
            response.error.message))