### Full and extensive analysis can be found in the file 100-house-prices-pipeline.ipynb.

- [I. PLANNING](#I)
    - [I.1 Introduction](#I.1)
    - [I.2 Dataset Description](#I.2)
    - [I.3 Project assumptions](#I.3)
        - [I.3.1 Defining the problem](#I.3.1)
        - [I.3.2 Success metric](#I.3.3)
        - [I.3.3 Feasibility  of the ML application](#I.3.4)
- [II.DATA COLLECTION AND PREPARATION](#II)
    - [II.1 Import libraries and data files](#II.1)
    - [II.2 Exploratory Data Analysis (EDA)](#II.2)
- [III DATA PRE-PROCESSING (data cleaning)](#III)           
    - [III.1 Filling nulls](#III.1)
    - [III.2 Convert Types (Downcasting)](#III.2)
    - [III.3 Categorical data transformation](#III.3)
    - [III.4 Skewness of distributions](#III.4)
    - [III.5 Detect Outlier](#III.5)    
    - [III.6 Normalizing](#III.6)     
    - [III.7 Feature Selections](#III.7)    
- [IV DATA PROCESSING](#IV)
- [V MODEL ENGINEERING](#V)
    - [V.1 RandomForestRegressor](#V.1)
        - [V.1.1 RandomForestRegressor - Evaluation](#V.1.1)
    - [V.2 XGBRegressor](#V.2)  
        - [V.2.1 XGBRegressor - Evaluation](#V.2.1)
    - [V.3 LGBMRegressor](#V.3)
        - [V.3 LGBMRegressor - Evaluation](#V.3.1)
    - [V.4 CatBoostRegressor](#V.4)
        - [V.4 CatBoostRegressor - Evaluation](#V.4.1)    
     - [V.5 CatBoostRegressor](#V.5)
        - [V.5.1 CatBoostRegressor - Evaluation](#V.5.1)       
- [VI CONCLUSION](#VI)
   
   
I.1 Introduction
Ask a home buyer to describe their dream house, and they probably won't begin with the height of the basement ceiling or the proximity to an east-west railroad. But this playground competition's dataset proves that much more influences price negotiations than the number of bedrooms or a white-picket fence.

I.2 Dataset description
Full feature description is in eda.ipynb file

I.3 Project assumptions
I.3.1 Defining the problem
It is your job to predict the sales price for each house. For each Id in the test set, you must predict the value of the SalePrice variable.

I.3.2 Assessing the scope
The entire project was done in Python, using Jupyter. Submissions are evaluated on Root-Mean-Squared-Error (RMSE) between the logarithm of the predicted value and the logarithm of the observed sales price. (Taking logs means that errors in predicting expensive houses and cheap houses will affect the result equally.)

The feasibility of the project plan should be assessed to decide whether you are able to build a reliable predictive model with such a small sample of data. Or, can we get new data?

Feature engineering will be used for this purpose to obtain a more complete set of predictive attributes. An additional aspect that will affect the assessment of the project feasibility is the provided test data set, which will be used to verify the quality of the obtained predictive model.


### Author Details:
- Name: Adam Smulczyk
- Email: adam.smulczyk@gmail.com
- Profile: [Github](https://github.com/AdamSmulczyk)
- [Github Repository](https://github.com/AdamSmulczyk/002b_House_Prices)
