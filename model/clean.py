# Cleans and regularizes the data and outputs to 'train_clean.csv'
# Removes the "profanity" label - changes it to hate or not hate

import pandas as pd
import re

train = pd.read_csv('labeled_data.csv')

def  clean_text(df, text_field):
    df[text_field] = df[text_field].str.lower()
    df[text_field] = df[text_field].apply(lambda elem: re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", elem))  
    return df

# 1 represents hate speech, 0 represents profanity or normal speech
def isHate(x):
	if (x == 0):
		return 1
	else:
		return 0


train_clean = clean_text(train, "tweet")
train_clean = train_clean.drop("Unnamed: 0", 1)
train_clean['label'] = train_clean['label'].map(lambda c : isHate(c))

train_clean.to_csv('train_clean.csv')
# print("Training Set:"% train_clean.columns, train_clean.shape, len(train_clean))
# print(train_clean.head(10))
