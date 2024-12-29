import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def pairplot(df, hue:str=None, save_dir:str="."):
    plt.figure(figsize=(10, 6))
    sns.pairplot(df, hue=hue)
    plt.savefig(os.path.join(save_dir, "iris_pair.png"))

def violinplot(df, 
               hue:str=None, 
               y:str=None, 
               save_dir:str="."):
    plt.figure(figsize=(10, 6))
    sns.violinplot(df, x=hue, y=y, hue=hue)
    plt.savefig(os.path.join(save_dir, "iris_violin.png"))

def main():
    # load data
    df_iris = pd.read_csv("data/iris.csv", index_col=0)

    # create images directory
    save_dir = "images"
    os.makedirs(save_dir, exist_ok=True)

    # save plots
    pairplot(df_iris, hue="target", save_dir=save_dir)
    violinplot(df_iris, hue="target", save_dir=save_dir, y="sepal length (cm)")


main()