from flask import Flask
from flask import render_template, request

# modeling packages
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

###########################################################################################
# Flask Setup
###########################################################################################

app = Flask(__name__)

###########################################################################################
# Flask Routes
###########################################################################################

@app.route('/predict', methods=['GET','POST'])
def predict():
    data = {}   # data object to be passed back to the web page
    if request.form:
        # get the form data
        form_data = request.form
        data['form'] = form_data
        predict_married = form_data['predict_married']
        predict_education = form_data['predict_education']
        predict_credit = form_data['predict_credit']

        print(data)

        # convert the input from text to binary
        if predict_married == 'Single':
            married = 0
        else:
            married = 1

        if predict_education == 'Graduated':
            education = 1
        else:
            education = 0

        if predict_credit == 'Bad':
            credit = 0
        else:
            credit = 1

        input_data = np.array([married, education, credit])

        # get prediction
        prediction = L1_logistic.predict_proba(input_data.reshape(1, -1))
        prediction = prediction[0][1] # loan status
        data['prediction'] = '{:.1f}% Approval Probability'.format(prediction * 100)

    return render_template('index.html', data=data)

###########################################################################################
# Main Behavior
###########################################################################################

if __name__ == "__main__":

    # Build an ML model. Key predictors = 'Married', 'Education', 'Credit_History'
    loan_df = pd.read_csv('Data/clean_data.csv')

    # # convert 'Married' column data to binary values
    # loan_df['Married_binary'] = loan_df['Married'].map({'Yes': 1, 'No': 0})
    # # convert 'Education' column data to binary values
    # loan_df['Education_binary'] = loan_df['Education'].map({'Graduate':1,'Not Graduate':0})

    # choose our features and create a test and train sets
    features = ['Married', 'Education', 'Credit_History', 'Loan_Status']
    
    train_df, test_df = train_test_split(loan_df)
    train_df = train_df[features]
    test_df = test_df[features]

    features.remove('Loan_Status')

    X_train = train_df[features]
    X_train = train_df[features]
    y_train = train_df['Loan_Status']
    X_test = test_df[features]
    y_test = test_df['Loan_Status']

    # fit the model
    L1_logistic = LogisticRegression(C=1.0, penalty='l1', solver='liblinear')
    L1_logistic.fit(X_train, y_train)

    # check the performance
    target_names = ['Denied', 'Approved']
    y_pred = L1_logistic.predict(X_test)
    print(classification_report(y_test, y_pred, target_names=target_names))

    app.run(debug=True)