# COIN_FLASK_BE

Read: https://code.visualstudio.com/docs/python/tutorial-flask to setup env

Insert folder "models" with following models:
- https://drive.google.com/file/d/1dc81-3yQBJv6GV4ALlX6Af3zoG5F4ZTZ/view?usp=sharing
- 152_3_01: https://drive.google.com/drive/u/0/folders/1S8Kyli2W3cx0t54x6kMRtD9Sq9181TLU
Insert folder "images" and "croppedImages"

To run:
1) python -m flask run --host:0.0.0.0
2) python3 -m flask run --host:0.0.0.0

Maybe:
pip install tensorflow
pip install opencv-python
pip install imagaAI
pip install -U numpy 

.. Wahrscheinloch noch andere pip, war n Pain in the Ass (TRUE)


Postman: POST http://localhost:5000/predictEmotion
- Body:
    - Key: file
    - Value: Bild auswählen
