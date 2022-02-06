# EndHate

EndHate is an API that uses machine learning to decide whether text is hate speech or not. The model is built using the scikit-learn library and a
stochastic gradient descent classifier. The API is built on a Flask webserver.

## Model
The model was trained on a dataset of labeled twitter posts. [Here](https://www.kaggle.com/mrmorj/hate-speech-and-offensive-language-dataset) is the link to the kaggle dataset.

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


