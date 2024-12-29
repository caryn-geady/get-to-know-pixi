from sklearn import datasets
import pandas as pd
import os

def load_iris():
    # load Iris dataset
    iris = datasets.load_iris(as_frame=True)
    print(iris)
    return pd.concat([iris.data, iris.target], axis=1)

def save_iris(df, path):
    # create data directory
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # save data
    df.to_csv(path)

def main():
    # load data
    df_iris = load_iris()
    save_iris(df_iris, "data/iris.csv")

main()