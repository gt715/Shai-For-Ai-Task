import matplotlib.pyplot as plt
import numpy as np


class DataCorrelation:
    def __init__(self, df):
        self.df = df

#  calculate_and_visualize_correlation

    def calculate_and_visualize_correlation(self):
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        numeric_cols.remove('Id')  # remove the id col from the new dataframe

        for col in numeric_cols:
            if col != 'TotalPayBenefits': 
                correlation = self.df['TotalPayBenefits'].corr(self.df[col])
                print(f'Correlation between Salary and {col}: {correlation}')
                plt.figure(figsize=(5, 5))
                plt.scatter(self.df['TotalPayBenefits'], self.df[col])				
                plt.xlabel('Salary')
                plt.ylabel(col)
                plt.title(f'Salary vs {col}')
                plt.show()
