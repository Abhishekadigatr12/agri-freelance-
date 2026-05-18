from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import tensorflow as tf
import tensorflow as tf
from pathlib import Path

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.2
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)
# Keras
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH ='./model_vgg16.h5'

# Load your trained model
model = load_model(MODEL_PATH)

class_folders = sorted(glob.glob('./dataset/train/*'))
class_names = [Path(folder).name for folder in class_folders]




def model_predict(img_path, model):
    
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    # Match the preprocessing used during VGG16 training
    x = preprocess_input(x)

    preds = model.predict(x)
    preds=np.argmax(preds, axis=1)
    
    
    preds=preds[0]
    print(f"Result of prediction = {preds}")
    
    if 0 <= preds < len(class_names):
        return class_names[preds]

    return str(preds)


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('home.html')


@app.route('/about.html', methods=['GET'])
def about():
    # Main page
    return render_template('about.html')
	
	
	
@app.route('/home.html', methods=['GET'])
def home():
    # Main page
    return render_template('home.html')
	

@app.route('/logout.html', methods=['GET'])
def logout():
    # Main page
    return render_template('login.html',msg="logout")
	


@app.route('/login.html', methods=['GET', 'POST'])
def login():

	if request.method == 'POST':
		username=request.form['username']
		password=request.form['password']
		
		if username=="admin" and password=="admin":
			return render_template('index.html')
		else:
			return render_template('login.html',msg="failed")
		
	else:
		return render_template('login.html')
		
@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        result=preds
        return result
    return None


if __name__ == '__main__':
    app.run(port=5001,debug=True)
