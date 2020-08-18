# Loan Prediction Using selected Machine Learning Algorithms
![account](Images/account.jpg)
------------------------------
Loan Probability with Machine Learning, without a credit score ding!
<h1> ️Contributers </h1>

[<sub><b>Anastasia V</b></sub>](https://github.com/AnastasiaRV)<br/><img src="https://avatars0.githubusercontent.com/u/61332049?s=400&v=4" width="100px;"/><br/>

[<sub><b>Anna G</b></sub>](https://github.com/heyannag)<br/><img src="https://avatars1.githubusercontent.com/u/61209602?s=460&u=5dbd7647e94f58132f5f6e0274767e98fc11bd94&v=4" width="100px;"/><br/>
 
[<sub><b> Masita M </b></sub>](https://github.com/masitamohamad)<br/><img src="https://avatars3.githubusercontent.com/u/60247306?s=400&u=ae1efcb5e0637cdd4a2afe1c7ab45c9e7eb20bd6&v=4" width="100px;"/><br/>
 
[<sub><b> Catie C </b></sub>](https://github.com/csidneyclark)<br/><img src="https://avatars0.githubusercontent.com/u/61070215?s=400&v=4" width="100px;"/><br/>
 
[<sub><b> Matt O </b></sub>](https://github.com/oconnormatt781)<br/><img src="https://avatars1.githubusercontent.com/u/59668093?s=460&v=4" width="100px;"/><br/>


![loan_predictor](Images/loan_predictor.gif)


# Database Discovery 
Source of Dataset: The dataset for this project is retrieved from [Kaggle](https://www.kaggle.com/altruistdelhite04/loan-prediction-problem-dataset), the home of Data Science. 


Columns | Description | Key Parameter Y/N
:-----|:----- |:-----:
`Loan_ID` | Unique Load ID | N
`Gender` | Male/Female | N
`Married`| Maritail Status Y/N) | Y
`Dependents`| Number of Dependants Claimed | N
`Education` | College Graduate Y/N | Y
`Self_Employed`| Self-Employed Y/N | N
`Applicant_Income` | Applicant Annual Income | Y
`Coapplicant_Income` | Co-Applicant's Income | Y
`Loan_Amount`| Loan Amount in Thousands | Y
`Loan_Amount_Term` | Loan Term in Months | N
`Credit_History`| Meets Criteria (1;0) | N
`Property_Area` | Urban, Semi-Urban and Rural | N
`Loan_Status` | Approved Y/N | Y

# Machine Learning Models 
<b>The problem at hand:</b> The major aim of this project is to predict which of the customers will receive a loan or not. Therefore, this is a supervised classification problem to be trained with algorithm:
<b>Logistic Regression</b>


<b>Predictor problem:</b> linear regression will answer the dollar amount do you qualify for based on total applicant income by using algorithm:
<b>Linear regression</b>



## How it all works together
![image.png](Images/process_diagram.png)

## Data Cleaning
![data_cleaning](Images/data_cleaning.png)
Read the data and checked the shape. Oh! it has 614 rows and 13 columns. That’s 12 features

<b>Missing Values:</b> Check where there are missing values and fix them appropriately
   
    '''
     df.isnull().sum() #uncover the amount of null values
     df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].mean()) # fill in null 'LoanAmount' with column mean
     df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].median()) # fill in null 'Credit_History' with column mean
     df.dropna(inplace=True) 
 
 Now all missing values are dropped to avoid errors in the model.

## Exploring the Data

![married](Images/Loan_Status_Married.png)<br/>
As seen above, a Married Person has more chance of getting the loan.

![graduate](Images/Loan_Status_Education.png)<br/>
Also, a Graduate level degree give the individual more chance of getting the loan. 

## Encoding to numeric Data; getting ready for model training

    '''
    code_numeric = {‘Male’: 1, ‘Female’: 2,
    ‘Yes’: 1, ‘No’: 2,
    ‘Graduate’: 1, ‘Not Graduate’: 2,
    ‘Urban’: 3, ‘Semiurban’: 2,’Rural’: 1,
    ‘Y’: 1, ’N’: 0,
    ‘3+’: 3}
    df_train = df_train.applymap(lambda s: code_numeric.get(s) if s in code_numeric else s)
    df_test = df_test.applymap(lambda s: code_numeric.get(s) if s in code_numeric else s)
    #drop the uniques loan id
    df_train.drop(‘Loan_ID’, axis = 1, inplace = True)


<b>Heatmap:</b> Showing the correlations of features with the target. No correlations are extremely high. The correlations between LoanAmount and ApplicantIncome can be explained.
![heatmap](Images/Correlation_Matrix.png)

## Using Logistic Regression

    '''
    model = LogisticRegression()
    model.fit(X_train,y_train)

    lr_prediction = model.predict(X_test)
    print('Logistic Regression accuracy = ', metrics.accuracy_score(lr_prediction,y_test))
 Logistic Regression accuracy =  0.7914110429447853
 
## Using Linear Regression

    '''
    model = LinearRegression()
    model.fit(X_train,y_train)

    lr_prediction = model.predict(X_test)
