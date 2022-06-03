# COIN_FLASK_BE

Read: https://code.visualstudio.com/docs/python/tutorial-flask to setup env

Insert folder "models" with following models:
- https://drive.google.com/file/d/1dc81-3yQBJv6GV4ALlX6Af3zoG5F4ZTZ/view?usp=sharing
- https://drive.google.com/file/d/1dc81-3yQBJv6GV4ALlX6Af3zoG5F4ZTZ/view?usp=sharing

Insert folder "images" and "croppedImages"

To run: python -m flask run

Maybe:
pip install tensorflow
pip install opencv-python
pip install imagaAI
pip install -U numpy 

.. Wahrscheinloch noch andere pip, war n Pain in the Ass


Postman: POST http://localhost:5000/predictEmotion
- Body:
    - Key: file
    - Value: Bild auswählen
