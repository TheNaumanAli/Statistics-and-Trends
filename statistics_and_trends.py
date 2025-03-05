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
   Create and save relational plots including a scatter plot and a line plot between Ticket_Price and Age.
   """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

   # Making Scater plot
    sns.scatterplot(data=df, x='Ticket_Price', y='Age', alpha=0.7, ax=axes[0])
    axes[0].set_title("Scatter Plot: Ticket Price vs Age")
    axes[0].set_xlabel("Ticket Price ($)")
    axes[0].set_ylabel("Age (years)")
    axes[0].grid(True)

   # creating Line graph
    sns.lineplot(data=df, x='Ticket_Price', y='Age', ax=axes[1])
    axes[1].set_title("Line Plot: Ticket Price vs Age")
    axes[1].set_xlabel("Ticket Price ($)")
    axes[1].set_ylabel("Age (years)")
    axes[1].grid(True)
    plt.tight_layout()
    plt.savefig('relational_plot.png')
    plt.show()
    plt.close()
    return


def plot_categorical_plot(df):
    """
       Create and save a categorical plot (box plot) showing Age distribution by Purchase_Again status.
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

   # plotting Bar graph and checking Count of purchase again by customer
    sns.countplot(x='Purchase_Again', data=df, ax=axes[0])
    axes[0].set_title('Bar Plot: Count of Purchase Again')
    axes[0].set_xlabel('Purchase Again (0 = No, 1 = Yes)')
    axes[0].set_ylabel('Count')
    axes[0].grid(True)

   # making a histogram for age distribution
    axes[1].hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
    axes[1].set_title('Histogram: Age Distribution')
    axes[1].set_xlabel('Age (years)')
    axes[1].set_ylabel('Frequency')
    axes[1].grid(True)

   # creating a pie chart for customer purchasing again
    purchase_counts = df['Purchase_Again'].value_counts()
    axes[2].pie(purchase_counts, labels=['No', 'Yes'], autopct='%1.1f%%', startangle=90, explode=[0.05, 0.05])
    axes[2].set_title('Pie Chart: Proportion of Customers Purchasing Again')

    plt.tight_layout()
    plt.savefig('categorical_plot.png')
    plt.show()
    plt.close()
    return

def plot_statistical_plot(df):
    """
   Create and save a statistical plot (pair plot) to visualize relationships 
   between Age, Ticket_Price, and Purchase_Again.
   """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

   # Creating a correlation heatmap
    sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm', ax=axes[0])
    axes[0].set_title('Correlation Heatmap')

   # Creating a violin plot for age distribution by purchase again
    sns.violinplot(x='Purchase_Again', y='Age', data=df, ax=axes[1])
    axes[1].set_title('Violin Plot: Age by Purchase Again Status')
    axes[1].set_xlabel('Purchase Again (0 = No, 1 = Yes)')
    axes[1].set_ylabel('Age (years)')
    axes[1].grid(True)

    plt.tight_layout()
    plt.savefig('statistical_plot.png')
    plt.show()
    plt.close()
    return

def statistical_analysis(df, col: str):
    """
        here we Perform statistical analysis to calculate a mean, standard deviation, skewness, and excess kurtosis of the specified column.
    """
    mean = df[col].mean()
    stddev = df[col].std()
    skew_value = ss.skew(df[col])
    excess_kurtosis_value = ss.kurtosis(df[col])   
    return mean, stddev, skew_value, excess_kurtosis_value


def preprocessing(df):
    # You should preprocess your data in this function and
    # make use of quick features such as 'describe', 'head/tail' and 'corr'.
    print(df.info())
    print(df.head())
    df = df.dropna()
    print("\nSummary Statistics:\n", df.describe())
    print("\nCorrelation Matrix:\n", df.select_dtypes(include=[np.number]).corr())
    return df

def writing(moments, col):
    """
        Printing the statistical analysis results, interpreting the skewness and kurtosis.
    """
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
         f'Standard Deviation = {moments[1]:.2f}, '
         f'Skewness = {moments[2]:.2f}, and '
         f'Excess Kurtosis = {moments[3]:.2f}.')
   
   # interpreting  skewness 
    if moments[2] > 0:
       skewness = "right skewed"
    elif moments[2] < 0:
       skewness = "left skewed"
    else:
       skewness = "not skewed"
   # checking kurtosis
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
    try:
        df = pd.read_csv('data.csv')
    except FileNotFoundError:
        print("Error: The file 'data.csv' was not found.")
        return
    df = preprocessing(df)
    col = 'Age'
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return

if __name__ == '__main__':
    main()
