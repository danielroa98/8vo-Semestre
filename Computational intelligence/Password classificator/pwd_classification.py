import pandas as pd

# For text feature extraction
from sklearn.feature_extraction.text import TfidfVectorizer

# For creating a pipeline
from sklearn.pipeline import Pipeline

# Classifier Model (Logistic Regression)
from sklearn.linear_model import LogisticRegression

#adjust the data removing errors
import data_utils as utils
#utils.adjust_file('resources/data.csv','resources/data1.csv',)

# Read the File
''' Warning Msg:  Solve DtypeWarning: Columns have mixed types. Specify dtype option on import or set low_memory=False in Pandas
                - Solutions: SET THE LOW_MEMORY ARGUMENT OF READ_CSV TO FALSE'''
data = pd.read_csv('resources/data1.csv', low_memory=False)


print(data.info())
print(data["strength"].value_counts())
print(data.describe())



# Sequentially apply a list of transforms and a final estimator
classifier_model = Pipeline([
                ('tfidf', TfidfVectorizer(analyzer='char')),
                ('logisticRegression',LogisticRegression(multi_class='multinomial', solver='sag')),
])



train_set, test_set = utils.split_train_test(data,0.2)
print("test set size:", len(test_set))
print("train set size:",len(train_set))

# Features which are passwords
features_train = train_set.values[:, 1].astype('str')
features_test = test_set.values[:, 1].astype('str')

# Labels which are strength of password (target of classification)
labels_train = train_set.values[:, -1].astype('int')
labels_test = test_set.values[:, -1].astype('int')

# Fit the Model
classifier_model.fit(features_train, labels_train)

#predictions
predictions = classifier_model.predict(features_test)

from sklearn.metrics import accuracy_score
score = accuracy_score(labels_test,predictions) #score = classifier_model.score(features_test, labels_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(score))

from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(labels_test, predictions)
print(confusion_matrix)

input_data = ['faizanahmad','faizanahmad123','faizanahmad##','ajd1348#28t**','ffffffffff','kuiqwasdi','uiquiuiiuiuiuiuiuiuiuiuiui','mynameisfaizan','mynameis123faizan#','faizan','123456','abcdef']
res_predictions = classifier_model.predict(input_data)
print(res_predictions)
