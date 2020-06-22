import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\toto\Documents\A2019\VisionAPIDemo\GoogleCloudVision.json'

client = vision.ImageAnnotatorClient()

def detectText(img):
    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.document_text_detection(image=image)
    texts = response.full_text_annotation.text
   
    return texts


img = r'C:\Users\toto\Documents\A2019\VisionAPIDemo\img\SRITHAI (Packaging) 1.jpg'
print(detectText(img))