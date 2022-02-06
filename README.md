# EndHate

EndHate is an API that uses machine learning to decide whether text is hate speech or not. The model is built using the scikit-learn library and a
stochastic gradient descent classifier. The API is built on a Flask webserver.

## Files
The model and the training data are contained in the [```/model```](https://github.com/vikram-ak/EndHate/tree/master/model) folder. This folder also includes the data and the scripts used to train the model. 

## **Warning, the data contains very explicit text. View at your own risk.**
<br>

The [```/sever```](https://github.com/vikram-ak/EndHate/tree/master/server) folder contains the flask webserver which hosts the API.

The [```/demo```](https://github.com/vikram-ak/EndHate/tree/master/demo) folder contain the files for the demo webpage.
<br>
<br>

## Model
The model was trained on a dataset of labeled twitter posts. [Here](https://www.kaggle.com/mrmorj/hate-speech-and-offensive-language-dataset) is the link to the kaggle dataset. The data was cleaned using [```clean.py```](https://github.com/vikram-ak/EndHate/tree/master/model/model.py). The data includes many more normal examples than hate speech examples so the hate speech examples were upsampled.

[```model.py```](https://github.com/vikram-ak/EndHate/tree/master/model/model.py) creates and saves the model to ```trained_model.sav```. The Flask webserver then uses this model to make predictions on incoming requests. [```model.py```](https://github.com/vikram-ak/EndHate/tree/master/model/model.py) only needs to be run when updates to the algorithm are made (it is not run for each request).

<br>

## API

The main (and only) API endpoint is ```/input```. It is expecting a json object with one name value pair in the form:
```
{ text : 'yourText'}
```

The server will respond with this json object:
```
{ text : 'yourText',
  label : 0/1
}
```
If label is 1, EndHate thinks it is hate speech. If label is 0, EndHate thinks that it is not hate speech.


