from detecto import core, utils, visualize
from typing import Dict
from io import BytesIO
import numpy as np
from PIL import Image

# function to read the image file from the api input
def read_img(file: bytes):

    img = Image.open(BytesIO(file))

    return img

# prediction function
def prediction(image):

    model = core.Model.load('model_weights.pth', ['allianz'])
    predictions = model.predict(image)
    labels, boxes, scores = predictions
    x, y, w, h = boxes[0]
    image.crop((float(x), float(y), float(w), float(h))).save('output/img.jpg')

    return visualize.show_labeled_image(image, boxes[0], scores[0])
