from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report,confusion_matrix
import numpy as np
import pandas as pd

### Using Stratified k-fold
def EvalClassifiers(Name, X, y, n_splits=10, score = balanced_accuracy_score):
    
    df = pd.DataFrame()
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=1)
    
    for train_index, test_index in skf.split(X, y):
        
        df_sim = pd.DataFrame()
        Xtr, Xte = X[train_index], X[test_index]
        ytr, yte = y[train_index], y[test_index]
        
        # Process the data
        scaler = StandardScaler()
        Xtr = scaler.fit_transform(Xtr)
        Xte = scaler.transform(Xte)
                
        # Random Forest
        rf = RandomForestClassifier(n_estimators = 30).fit(Xtr,ytr)
        y_pred = rf.predict(Xte)
        df_sim["Random Forest"] = [score(yte,y_pred)]
        
        ada = AdaBoostClassifier(n_estimators=100, random_state=0).fit(Xtr,ytr)
        y_pred = ada.predict(Xte)
        df_sim["AdaBoost"] = [score(yte,y_pred)]
        
        decisiontree = DecisionTreeClassifier().fit(Xtr,ytr)
        y_pred = decisiontree.predict(Xte)
        df_sim["DecisionTree"] = [score(yte,y_pred)]
                        
                
        df = pd.concat([df,df_sim])
    df.to_csv("CSVs/%s.csv" % Name)
    
    return df


### Using 90-10 train-test split
def EvalClassifiers_9010(Name, Xtr, ytr, Xte, yte, score = balanced_accuracy_score):
    
    df = pd.DataFrame()
    df_sim = pd.DataFrame()
    
    # Process the data
    scaler = StandardScaler()
    Xtr = scaler.fit_transform(Xtr)
    Xte = scaler.transform(Xte)

    # Random Forest
    rf = RandomForestClassifier().fit(Xtr,ytr)
    y_pred = rf.predict(Xte)
    df_sim["Random Forest"] = [score(yte,y_pred)]
    
    print("Random Forest")
    print(classification_report(yte,y_pred))
    print(" ")
    
    ada = AdaBoostClassifier().fit(Xtr,ytr)
    y_pred = ada.predict(Xte)
    df_sim["AdaBoost"] = [score(yte,y_pred)]
    
    print("AdaBoost")
    print(classification_report(yte,y_pred))
    print(" ")
    
    decisiontree = DecisionTreeClassifier().fit(Xtr,ytr)
    y_pred = decisiontree.predict(Xte)
    df_sim["DecisionTree"] = [score(yte,y_pred)]
    print("DecisionTree")
    print(classification_report(yte,y_pred))
    print(" ")                        
                
    df = pd.concat([df,df_sim])
    df.to_csv("CSVs/%s.csv" % Name)
    
    return df


def EvalBestModel(best_model, X, y, n_splits=10, score = balanced_accuracy_score, Name = 'best_model'):
    
    df = pd.DataFrame()
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=1)
    
    for train_index, test_index in skf.split(X, y):
        
        df_sim = pd.DataFrame()
        Xtr, Xte = X[train_index], X[test_index]
        ytr, yte = y[train_index], y[test_index]
        
        # Process the data
        scaler = StandardScaler()
        Xtr = scaler.fit_transform(Xtr)
        Xte = scaler.transform(Xte)
                
        # Random Forest
        rf = best_model.fit(Xtr,ytr)
        y_pred = rf.predict(Xte)
        df_sim["Best Model"] = [score(yte,y_pred)]
        
                        
                
        df = pd.concat([df,df_sim])
    df.to_csv("CSVs/%s.csv" % Name)
    
    return df