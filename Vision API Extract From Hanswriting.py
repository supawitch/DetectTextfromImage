import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\toto\Documents\A2019\VisionAPIDemo\GoogleCloudVision.json'
client = vision.ImageAnnotatorClient()

# FOLDER_PATH = r'C:\Users\toto\Documents\A2019\VisionAPIDemo'
# IMAGE_FILE = '2.jpg'
FILE_PATH = r'C:\Users\toto\Documents\A2019\VisionAPIDemo\img\SRITHAI (Packaging) 1.jpg'

def detect(FILE_PATH):
    with io.open(FILE_PATH, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.document_text_detection(image=image)
    docText = response.full_text_annotation.text

    return docText

print(detect(FILE_PATH))



