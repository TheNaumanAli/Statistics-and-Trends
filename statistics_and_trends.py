"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    """
        Create and save a relational plot (scatter plot) between Ticket_Price and Age.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df, x='Ticket_Price', y='Age', alpha=0.7, ax=ax)
    ax.set_title("Scatter Plot: Ticket Price vs Age")
    ax.set_xlabel("Ticket Price ($)")
    ax.set_ylabel("Age (years)")
    ax.grid(True)
    plt.savefig('relational_plot.png')
    plt.close()
    return


def plot_categorical_plot(df):
    """
       Create and save a categorical plot (box plot) showing Age distribution by Purchase_Again status.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(data=df, x='Purchase_Again', y='Age', ax=ax)
    ax.set_title("Box Plot: Age Distribution by Purchase Again Status")
    ax.set_xlabel("Purchase Again (0 = No, 1 = Yes)")
    ax.set_ylabel("Age (years)")
    ax.grid(True)
    plt.savefig('categorical_plot.png')
    plt.close()
    return

def plot_statistical_plot(df):
    """
        Create and save a statistical plot (pair plot) to visualize relationships between Age, Ticket_Price, and Purchase_Again.
    """
    sns.pairplot(df[['Age', 'Ticket_Price', 'Purchase_Again']])
    plt.title("Pair Plot: Age, Ticket Price, and Purchase Again Status")
    plt.savefig('statistical_plot.png')
    plt.close()
    return

def statistical_analysis(df, col: str):
    """
        Perform statistical analysis to calculate mean, standard deviation, skewness, and excess kurtosis of the specified column.
    """
    mean = df[col].mean()
    stddev = df[col].std()
    skew_value = ss.skew(df[col])
    excess_kurtosis_value = ss.kurtosis(df[col])   
    return mean, stddev, skew_value, excess_kurtosis_value


def preprocessing(df):
    # You should preprocess your data in this function and
    # make use of quick features such as 'describe', 'head/tail' and 'corr'.
    print(df.select_dtypes(include=[np.number]).corr())  # Only numeric columns
    return df

def writing(moments, col):
    """
        Print the statistical analysis results and interpret the skewness and kurtosis.
    """
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
         f'Standard Deviation = {moments[1]:.2f}, '
         f'Skewness = {moments[2]:.2f}, and '
         f'Excess Kurtosis = {moments[3]:.2f}.')
   
   # Interpret skewness and kurtosis
    if moments[2] > 0:
       skewness = "right skewed"
    elif moments[2] < 0:
       skewness = "left skewed"
    else:
       skewness = "not skewed"
   
    if moments[3] > 0:
       kurtosis_type = "leptokurtic"
    elif moments[3] < 0:
       kurtosis_type = "platykurtic"
    else:
       kurtosis_type = "mesokurtic"
   
    print(f'The data was {skewness} and {kurtosis_type}.')
    return


def main():
    """
       Main function to load data, preprocess, generate plots, and perform statistical analysis.
   """
    df = pd.read_csv('data.csv')  # Replace 'data.csv' with the actual path to the dataset
    df = preprocessing(df)
  
    # Choose a column for statistical analysis (e.g., 'Age')
    col = 'Age'  # You can change this to analyze another column like 'Ticket_Price' or 'Number_of_Person'
  
    # Plot the graphsx
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
  
    # Perform statistical analysis and print results
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return


if __name__ == '__main__':
    main()
