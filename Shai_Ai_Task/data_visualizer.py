import matplotlib.pyplot as plt
import numpy as np

class DataVisualizer:

    def __init__(self, df, sub_df):
        self.df = df  
        self.sub_df = sub_df  

    def print_separator(self):
        print("#################################################\n")

# Histogram shows the freq of the Salaries

    def plot_salary_distribution(self):
        h = plt.hist(self.df['TotalPayBenefits'], bins=11, edgecolor='black')
        plt.title('Salary Distribution')
        plt.xlabel('Salary')
        plt.ylabel('Frequency')
        plt.show()

# A piechart to show the percnetage of employees with the same job 

    def plot_job_title_distribution(self):
        self.print_separator()
        sample_df = self.df.sample(n=383)
        ss = sample_df['JobTitle'].value_counts()
        ss = ss[ss > 5]
        print(ss)
        P1 = plt.pie(ss, labels=ss.index, autopct='%1.1f%%')
        plt.title('Employees by Job_Title')
        plt.show()

# A piechart shows the percnetage of the employees under the same Department

    def plot_department_distribution(self):
        self.print_separator()
        sd = self.sub_df['JobTitle'].value_counts()
        self.sub_df.loc[:, 'Department'] = np.where(self.sub_df['JobTitle'].str.contains('Fire Department', case=False), 'Fire Department',
        np.where(self.sub_df['JobTitle'].str.contains('Police Department', case=False), 'Police Department', 'Other'))
        self.sub_df = self.sub_df[~(self.sub_df['Department'] == 'Other')]
        z = self.sub_df['Department'].value_counts()
        print(z)
        plt.pie(z, labels=z.index, autopct='%1.1f%%')
        plt.title('Employees by Departments')
        plt.show()
        sub_df=self.sub_df
        return sub_df  # Returns the updated subset dataframe
