import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def automated_eda(file_path):

    # Load Dataset
    df = pd.read_csv(file_path)

    print("\n========== DATASET LOADED SUCCESSFULLY ==========\n")

    # First 5 Rows
    print("FIRST 5 ROWS OF DATASET:\n")
    print(df.head())

    # Dataset Information
    print("\n========== DATASET INFO ==========\n")
    print(df.info())

    # Missing Values
    print("\n========== MISSING VALUES ==========\n")
    print(df.isnull().sum())

    # Fill Missing Values
    for col in df.columns:

        # Numerical Columns
        if df[col].dtype == 'int64' or df[col].dtype == 'float64':
            df[col] = df[col].fillna(df[col].median())

        # Categorical Columns
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

    print("\nMissing values handled successfully!")

    # Statistical Summary
    print("\n========== STATISTICAL SUMMARY ==========\n")
    print(df.describe())

    # Correlation Heatmap
    numeric_df = df.select_dtypes(include=['int64', 'float64'])

    if not numeric_df.empty:

        plt.figure(figsize=(8, 6))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
        plt.title("Correlation Heatmap")
        plt.show()

    # Histograms
    numeric_df.hist(figsize=(10, 8))
    plt.suptitle("Histograms")
    plt.show()

    print("\n========== EDA COMPLETED SUCCESSFULLY ==========\n")

    return df


# MAIN PROGRAM
file_path = input("Enter CSV file name with extension: ")

automated_eda(file_path)