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
        relation of ticket and price, create by scatter plot and line plot
    """
    fig, axs = plt.subplots(1, 2, figsize=(16, 6))

    # Scatter plot to show relationship between  price of ticket and age of a person
    sns.scatterplot(data=df, x='Ticket_Price', y='Age', alpha=0.7, ax=axs[0])
    #setting title of scatter for description, labeling x and y axis
    axs[0].set_title("Scatter Plot: Ticket Price vs Age")
    axs[0].set_xlabel("Ticket Price ($)")
    axs[0].set_ylabel("Age (years)")
    axs[0].grid(True)

    # Line plot to show relationship between Ticket Price and Age
    sns.lineplot(data=df, x='Ticket_Price', y='Age', ax=axs[1])
    #setting title for line plot and labeling x and y axis for ticket and age
    axs[1].set_title("Line Plot: Ticket Price vs Age")
    axs[1].set_xlabel("Ticket Price ($)")
    axs[1].set_ylabel("Age (years)")
    axs[1].grid(True)
    #cleaning data to prevent overlap 
    plt.tight_layout()
    plt.savefig('relational_plot.png')
    plt.show()
    plt.close()


def plot_categorical_plot(df):
    """
        plotting catergorical plot between age of person and purchase again
    """
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))

    # Bar plot showing the count of customers who purchased again
    sns.countplot(x='Purchase_Again', data=df, ax=axs[0])
    #labelling x and y axis. x(purchase again: 1yes,0no),y to count persons
    axs[0].set_title('Bar Plot: Count of Purchase Again')
    axs[0].set_xlabel('Purchase Again (0 = No, 1 = Yes)')
    axs[0].set_ylabel('Count')
    axs[0].grid(True)

    # histogram for age distribution
    axs[1].hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
    #setting the title of histogram to age distribution
    axs[1].set_title('Histogram: Age Distribution')
    #labelling x(age),y(frequency of age group)
    axs[1].set_xlabel('Age (years)')
    axs[1].set_ylabel('Frequency')
    axs[1].grid(True)

    # pie chart showing the proportion of customers purchasing again
    purchase_counts = df['Purchase_Again'].value_counts()
    axs[2].pie(purchase_counts, labels=['No', 'Yes'], autopct='%1.1f%%', startangle=90, explode=[0.05, 0.05])
    axs[2].set_title('Pie Chart: Proportion of Customers Purchasing Again')
    #making good layout
    plt.tight_layout()
    #saving plot as categorical_ploy.png and then showing and after that closing
    plt.savefig('categorical_plot.png')
    plt.show()
    plt.close()

def plot_statistical_plot(df):
    """
    creating statistical plot between age, ticketprice and purchase
    """
    fig, axs = plt.subplots(1, 2, figsize=(16, 6))

    # Correlation heatmap for numerical features
    sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm', ax=axs[0])
    axs[0].set_title('Correlation Heatmap')

    # Violin plot showing age distribution by purchase again status
    sns.violinplot(x='Purchase_Again', y='Age', data=df, ax=axs[1])
    #setting the title of violin plot and labelling x and y axis
    axs[1].set_title('Violin Plot: Age by Purchase Again Status')
    axs[1].set_xlabel('Purchase Again (0 = No, 1 = Yes)')
    axs[1].set_ylabel('Age (years)')
    axs[1].grid(True)
    #adjusting the spacing and prventing overlap,saving plot as statistical_plot.png,displaying plot and then closing
    plt.tight_layout()
    plt.savefig('statistical_plot.png')
    plt.show()
    plt.close()

def statistical_analysis(df, col: str):
    """
        analysising the data to calculate  mean and standard deviation and skew and excess kurtosis of the specified column.
    """
    mean = df[col].mean()
    stddev = df[col].std()
    skew_value = ss.skew(df[col])
    excess_kurtosis_value = ss.kurtosis(df[col])   
    return mean, stddev, skew_value, excess_kurtosis_value


def preprocessing(df):
    # You should preprocess your data in this function and
    # make use of quick features such as 'describe', 'head/tail' and 'corr'.
    #printing basic info of data frame
    print(df.info())
    #printing first few rows
    print(df.head())
    # Remove rows with missing values
    df = df.dropna()
    # Display summary statistics and correlation matrix
    print("\nSummary Statistics:\n", df.describe())
    print("\nCorrelation Matrix:\n", df.select_dtypes(include=[np.number]).corr())
    return df

def writing(moment, col):
    """
        printing the statistical analysis ( skewness and kurtosis).
    """
    print(f'For the attribute {col}:')
    print(f'Mean = {moment[0]:.2f}, '
         f'Standard Deviation = {moment[1]:.2f}, '
         f'skew = {moment[2]:.2f}, and '
         f'Excess Kurtosis = {moment[3]:.2f}.')
   
   # checking if it is left or right skewed 
    if moment[2] > 0:
       skew = "right skewed"
    elif moment[2] < 0:
       skew = "left skewed"
    else:
       skew = "not skewed"
   # checking the kurtosis
    if moment[3] > 0:
       type = "leptokurtic"
    elif moment[3] < 0:
       type = "platykurtic"
    else:
       type = "mesokurtic"
   #printing
    print(f'The data was {skew} and {type}.')
    return


def main():
    """
       main function to load data, preprocess, generate plots, and perform statistical analysis.
    """
    #reading the file
    try:
        df = pd.read_csv('data.csv')
    except FileNotFoundError:
        print("The file 'data.csv'  not found.")
        return
    df = preprocessing(df)
    # Setting the column for analysing
    col = 'Age'
    # Generate and save various plots.
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    # performing stats analysing and writing the results
    moment = statistical_analysis(df, col)
    writing(moment, col)
    return

if __name__ == '__main__':
    main()
