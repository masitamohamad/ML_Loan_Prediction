# Loan Prediction Model 

## Project Members
* Anastasia
* Anna
* Catie
* Masita 
* Matthew


## Machine Learning Model Project Plan 

* [Database Discovery](#DatabaseDiscovery)
* [Define the Problem](#DefinetheProblem)  
* [Machine Learning | Model Selection](#MachineLearningmodelselection)
* [Train and Test Model](#TrainandTestModel)
* [Tune the Training Model](#TunetheTrainingModel)
* [Apply Chosen Model](#ApplyChosenModel)
* [Save and Load Model | scikit-learn](#SaveandLoadModelscikit-learn)
* [Python File to Serve the Data](#PythonFiletoServetheData)
* [Develop index.html](#Developindex.html)

# Database Discovery 
Data Source: [Kaggle](https://www.kaggle.com/altruistdelhite04/loan-prediction-problem-datasetSource)

Data Fields | DType | Key Parameter Y/N
:-----:|:-----: |:-----:
`Loan_ID` | object | N
`Gender` | object | N
`Married`| object | Y
`Dependents`| object | Y
`Education` | object | Y
`Self_Employed`| object | N
`Applicant Income` | int64 | Y
`Coapplicant_Income` | float64 | N
`Loan_Amount`| float64 | Y
`Loan_Amount_Term` | float64 | N
`Credit_History`| float64 | N
`Property_Area` | object | Y
`Loan_Status` | object | Y

## Define the Problem
There are two parts to the question, one is binary (yes/no) and one is predictive (how much)
Binary problem – logistic regression will answer “do you qualify”Predictor problem – linear regression will answer “based on your income what do you qualify for”Machine Learning Model Selection
Logistic regression 
Linear regression

## Presentation
GitHub readme populated with key technical information (visuals) on our process of discovery, analysis, and model selection.
Website:
1.Landing page HTML where visitors to the website will interact with the website and enter answers to the key binary predictor parameters (Married, Income, Property, Dependents, Education) 
2.HTML page for “NO you do not qualify” – very dramatic red
3.HTML page for “YES you do qualify, now let’s find out how much of a loan youwill qualify for”
a.This is the page that will use the linear regression model using the two key parameters for Income, Loan Amountb.Visitors to the site will enter an income amount and the site will output the probable loan amount they will qualify for

