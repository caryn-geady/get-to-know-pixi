from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.metrics import roc_auc_score

import os
import joblib
import pandas as pd

def train_lr(X, y):
    # train logistic regression model
    model = LogisticRegression()
    model.fit(X, y)
    return model

def train_svm(X, y):
    # train support vector machine model
    model = SVC(probability=True)
    model = model.fit(X, y)
    return model

def train_kmeans(X, y):
    # train kmeans model
    model = KMeans(n_clusters=3)
    model.fit(X, y)
    return model

def main():
    # load data
    df_iris = pd.read_csv("data/iris.csv", index_col=0)

    # split data into train and test sets
    X_train, _, y_train, _ = train_test_split(df_iris.drop("target", axis=1), df_iris["target"], test_size=0.2, random_state=42, stratify=df_iris["target"])

    # train models
    model_lr = train_lr(X_train, y_train)
    model_svm = train_svm(X_train, y_train)
    model_kmeans = train_kmeans(X_train, y_train)

    # make save directory
    save_dir = "data/models"
    os.makedirs(save_dir, exist_ok=True)

    # save models
    joblib.dump(model_lr, os.path.join(save_dir, "lr.joblib"))
    joblib.dump(model_svm, os.path.join(save_dir, "svm.joblib"))
    joblib.dump(model_kmeans, os.path.join(save_dir, "kmeans.joblib"))

main()