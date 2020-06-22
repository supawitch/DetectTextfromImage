import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\toto\Documents\A2019\VisionAPIDemo\GoogleCloudVision.json'
client = vision.ImageAnnotatorClient()

FOLDER_PATH = r'C:\Users\toto\Documents\A2019\VisionAPIDemo\img'
IMAGE_FILE = 'SRITHAI (Packaging) 1.jpg'
FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)
response = client.document_text_detection(image=image)

docText = response.full_text_annotation.text
print(docText)

pages = response.full_text_annotation.pages
for page in pages:
    z = 1
    
    for block in page.blocks:
        
        print('block confidence:', z)
        z += 1
        # if z == 40:
        #     print(z)
        #     print('block confidence:', block.confidence)
        y = 1
        for paragraph in block.paragraphs:
            print('paragraph confidence:', y)
            #print('paragraph confidence:', paragraph.confidence)
            y += 1
            for word in paragraph.words:
                word_text = ''.join([symbol.text for symbol in word.symbols])
                
                print('Word text: {0} '.format(word_text))

                # for symbol in word.symbols:
                #     print('\tSymbol: {0} (confidence: {1}'.format(symbol.text, symbol.confidence))

########################################################################################################            

import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd
import sys

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\toto\Documents\A2019\VisionAPIDemo\GoogleCloudVision.json'
client = vision.ImageAnnotatorClient()

FOLDER_PATH = r'C:\Users\toto\Documents\A2019\VisionAPIDemo\img'
IMAGE_FILE = 'SRITHAI (Packaging) 1.jpg'
FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

def text(FILE_PATH):
    with io.open(FILE_PATH, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.document_text_detection(image=image)

    docText = response.full_text_annotation.text
    #print(docText)
    pages = response.full_text_annotation.pages
    for page in pages:
        for block in page.blocks:
            #print('{block} block confidence:', block.confidence)
            for count in range (1, pages.blocks, 1):
                print(count)

            for paragraph in block.paragraphs:
                print('{paragraph}paragraph confidence:', paragraph.confidence)

                
                for word in paragraph.words:
                    word_text = ''.join([symbol.text for symbol in word.symbols])
                    #print(word_text)
                    print(' {0} '.format(word_text))

                    #for symbol in word.symbols:
                        #print('\tSymbol: {0} (confidence: {1}'.format(symbol.text, symbol.confidence))
    return docText,block,count

print(text(FILE_PATH))
                
            
