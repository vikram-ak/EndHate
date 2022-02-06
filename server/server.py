from flask import Flask, send_from_directory
from flask import request
from flask import render_template
import json
import pandas as pd
import numpy as np
import pickle
import os.path


# relative path to saved model file
MODEL_FILE_PATH = '../model/trained_model.sav'

# initializing app
app = Flask(__name__)

# uses the model to make a prediction based on input text
def isHate(text):
	arr = np.array([text])
	ser = pd.Series(arr)

	ans = model.predict(ser)
	out = ans[0]
	return str(out)


# landing page endpoint
@app.route('/', methods=['GET'])

def home():
	return render_template('home.html')

# api endpoint for text input
@app.route('/input/', methods=['POST'])

def input():
	data = request.get_json()

	text = data['text']

	out = {
		"text" : text,
		"label": isHate(text)
	}
	return json.dumps(out) 


if __name__ == '__main__':
	model = pickle.load(open(os.path.dirname(__file__) + MODEL_FILE_PATH, 'rb'))
	app.run()