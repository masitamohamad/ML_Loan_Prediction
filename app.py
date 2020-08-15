from flask import Flask
from flask import render_template, request

# modeling packages
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.externals import joblib

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

    lr_prediction = joblib.load("model.pkl") # Load "model.pkl"
    print ('Model loaded')

    
    if request.form:
        # get the form data
        form_data = request.form
        data['form'] = form_data
        predict_married = form_data['predict_married']
        predict_education = form_data['predict_education']
        predict_credit = form_data['predict_credit']
        predict_income = form_data['predict_income']
        
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

        #######################################################################
        # Linear Regression

        predict_income = np.array(float(form_data['predict_income']))
        predict_income = predict_income.reshape(1, -1)

        loan_amount = lr_prediction.predict(predict_income)
        print(loan_amount)

        loan_amount_value = round(loan_amount[0][0]*1000,2)
        data['linearprediction'] = "${:,.2f}".format(loan_amount_value)

    return render_template('index.html', data=data)

###########################################################################################
# Main Behavior
###########################################################################################

if __name__ == "__main__":

    # Build an ML model. Key predictors = 'Married', 'Education', 'Credit_History'
    loan_df = pd.read_csv('Data/clean_data.csv')

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


###########################################################################################
    app.run(debug=True)