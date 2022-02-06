import pandas as pd
import numpy as np
from sklearn.utils import resample
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score
import pickle

# loading cleaned data

clean = pd.read_csv('train_clean.csv')

# upscaling minority to account for imbalanced data
majority = clean[clean.label==0]
minority = clean[clean.label==1]
minority_upsampled = resample(minority, 
                                replace=True,    
                                n_samples=len(majority),   
                                random_state=123)
train_upsampled = pd.concat([minority_upsampled, majority])
print(train_upsampled['label'].value_counts())

# creating training pipeline
pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf',  TfidfTransformer()),
    ('nb', SGDClassifier()),])

# separating data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(train_upsampled['tweet'],
                                                    train_upsampled['label'],random_state = 0)


# training and saving the model
model = pipeline.fit(X_train, y_train)
pickle.dump(model, open('trained_model.sav', 'wb'))

# testing model
# y_predict = model.predict(X_test)
# print(y_predict)
# print(f1_score(y_test, y_predict))
# print(accuracy_score(y_test, y_predict))
