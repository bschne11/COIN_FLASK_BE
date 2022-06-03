import io
import numpy as np
import os

import torch
import torch.nn as nn

import torchvision.transforms as transforms
import torchvision.models as models

from PIL import Image


# ToDo: Move to GPU?
model_path = "./models/resnet152_3_01"
resnet152_pretrained_loaded = models.resnet152(pretrained=True)
resnet152_pretrained_loaded.fc = nn.Linear(in_features=2048, out_features=3)
resnet152_pretrained_loaded.load_state_dict(torch.load(model_path))
resnet152_pretrained_loaded.eval()

_CLASSES = {
    0: 'Neutral',
    1: 'Relaxed',
    2: 'Anger_Fear'
}

def predict(imagePath):

    # Open the image, transform it and call toTensor
    img = Image.open(imagePath)

    transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((224, 224)),
    ])

    image = transform(img).float()
    image = image.unsqueeze(0)

    # ToDo: Move to GPU?
    # Predict the Emotion
    with torch.no_grad():
        prediction = resnet152_pretrained_loaded(image)
    
    probs = torch.softmax(prediction, dim=1)
    print(probs)
    # Get the Label and Probabilities of All Emotions
    emotion_highest = _CLASSES[np.argmax(prediction).item()]
    highest_pred = torch.max(probs).item()

    second_highest_pred, index = torch.kthvalue(probs, 2)
    second_highest_pred = second_highest_pred.item()
    emotion_second_highest = _CLASSES[index.item()]

    emotion_lowest = _CLASSES[np.argmin(prediction).item()]
    lowest_pred = torch.min(probs).item()

    # Save all information in a dictionary
    rest_emotions=[dict(probability=second_highest_pred, second_highest=emotion_second_highest), dict(lowest=emotion_lowest, probability=lowest_pred)]

    # Finally delete the image
    try: 
        os.remove(imagePath)
    except: 
        pass

    return emotion_highest, highest_pred, rest_emotions