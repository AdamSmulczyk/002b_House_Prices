#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from HP_models import *
from data_processor import preprocess_data


# In[2]:


def main():
    print('-' * 80)
    print('train')
    
    print("Preprocessing data...")
    train_file = 'train.csv'
    train = preprocess_data(train_file)
   
    X = train.drop(columns=['Id', 'SalePrice'])
    y = train['SalePrice']
 
    SEED = 42
#     XGB_Params = {'max_depth': 5, 
#               'min_child_weight': 11, 
#               'learning_rate': 0.02267914412755093,
#               'subsample': 0.9, 
#               'penalty': 'l2', 
#               'n_estimators': 100,
#               'gamma': 0.08,
#               'random_state': SEED}

    print("Initializing workflow...")
#     RFC_1 = RandomForestModel(n_estimators=42, random_state=SEED)
#     XGB_2 = XGBoostModel(**XGB_Params)
    
#     voting_estimators = [('RandomForest', RFC_1.model), ('XGBoost', XGB_2.model)]
#     workflow_voting = Workflow_8()
#     workflow_voting.run_workflow(
#         model_name='VotingModel',
#         model_kwargs={'estimators': voting_estimators,  'weights': [1.0, 2.0]},
#         X=X,
#         y=y,
#         test_size=0.2,
#         random_state=42,
#         scoring='r2'
#     )
    
    XGB_1 = Workflow_HP()
    XGB_1.run_workflow(
        model_name='RandomForestModel',
#         model_kwargs=XGB_Params,
       model_kwargs= {'random_state': SEED},    
        X=X,
        y=y,
        test_size=0.2,
        random_state=42,
        scoring='r2'
    )
    
    
if __name__ == "__main__":
    main()

