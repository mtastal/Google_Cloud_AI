import io
import os
from google.cloud import vision
from google.cloud.vision import types
client=vision.ImageAnnotatorClient()

file_name=os.path.join(
os.path.dirname(__file__),
'car.jpg')

with io.open(file_name,'rb') as image_file:
 content = image_file.read()

image = types.Image(content=content)
reponse = client.label_detection(image=image)
labels = reponse.label_annotations

print("Labels:")

for label in labels:
    
    print (label.decription)



