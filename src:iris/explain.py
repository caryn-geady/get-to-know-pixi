import joblib
import os

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import roc_auc_score, auc, precision_recall_curve, accuracy_score
from sklearn.model_selection import train_test_split
from yellowbrick.cluster.silhouette import silhouette_visualizer

def load_models(dir_path):
    # load models
    model_lr = joblib.load(os.path.join(dir_path, "lr.joblib"))
    model_svm = joblib.load(os.path.join(dir_path, "svm.joblib"))
    model_kmeans = joblib.load(os.path.join(dir_path, "kmeans.joblib"))
    
    return model_lr, model_svm, model_kmeans

def metrics(model, X, y):
    # calculate roc auc score
    y_hat = model.predict_proba(X)#[:, 1]
    auroc = roc_auc_score(y, y_hat, multi_class='ovr')
    accuracy = accuracy_score(y, model.predict(X))

    print(f"Model: {model}")
    print(f"AUROC: {auroc}")
    print(f"Accuracy: {accuracy}")
    print("\n")

def silhouette(model, X):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    # calculate silhouette score
    silviz = silhouette_visualizer(model, X, show=False, ax=ax)
    print(f"Silhouette Score: {silviz.silhouette_score_}")

    fig.savefig("images/silhouette.png")

def plot_predictions(X, y, y_hat, save_path="images/predictions.png"):
    X = X.to_numpy()
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y_hat)
    plt.savefig(save_path)

def main():
    lr, svm, km = load_models("data/models")

    # load data
    df_iris = pd.read_csv("data/iris.csv", index_col=0)
    _, X_test, _, y_test = train_test_split(df_iris.drop("target", axis=1), df_iris["target"], test_size=0.2, random_state=42, stratify=df_iris["target"])

    # calculate metrics
    metrics(lr, X_test, y_test)
    metrics(svm, X_test, y_test)
    silhouette(km, X_test)

    # plot predictions
    plot_predictions(X_test, y_test, lr.predict(X_test), save_path="images/lr_pred.png")
    plot_predictions(X_test, y_test, svm.predict(X_test), save_path="images/svm_pred.png")
    plot_predictions(X_test, y_test, km.predict(X_test), save_path="images/km_pred.png")

main()
