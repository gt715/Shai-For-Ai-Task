import matplotlib.pyplot as plt
import pandas as pd


class DataAnalyzer:
    def __init__(self, df, sub_df):
        self.df = df
        self.sub_df = sub_df

    def print_separator(self):
        print("#################################################\n")

# Calculates the summary statistics of the salaries grouped by the year

    def group_by_year(self):
        self.print_separator()
        sm = self.df.groupby('Year')['TotalPayBenefits'].agg(['mean', 'median', 'std'])
        print(sm)

# Calculates the summary statistics of the salaries grouped by the Department

    def group_by_department(self):
        self.print_separator()
        smz = self.sub_df.groupby('Department')['TotalPayBenefits'].agg(['mean','median','std'])
        print(smz)

# Calculates the summary statistics of the salaries grouped by the (Departmebts_Year)

    def group_by_department_year(self):
        self.print_separator()
        sdf = self.sub_df.groupby(['Department','Year'])['TotalPayBenefits'].agg(['mean','median','std'])
        print(sdf)

# Compares between the previous means values

    def calculate_average_salary(self):
        self.print_separator()
        mean1 = self.df.groupby('Year')['TotalPayBenefits'].mean()
        mean2 = self.sub_df.groupby('Department')['TotalPayBenefits'].mean()
        mean3 = self.sub_df.groupby('Year')['TotalPayBenefits'].mean()
        mean4 = self.sub_df.groupby(['Department','Year'])['TotalPayBenefits'].mean()
        df_mean1 = mean1.reset_index().rename(columns={'TotalPayBenefits': 'mean1'})
        df_mean2 = mean2.reset_index().rename(columns={'TotalPayBenefits': 'mean2'})
        df_mean3 = mean3.reset_index().rename(columns={'TotalPayBenefits': 'mean3'})
        df_mean4 = mean4.reset_index().rename(columns={'TotalPayBenefits': 'mean4'})
        df_means = pd.merge(df_mean1, df_mean4, on='Year', how='outer')
        df_means = pd.merge(df_means, df_mean2, on='Department', how='outer')
        df_means = pd.merge(df_means, df_mean3, on='Year', how='outer')
        print(df_means)

# visualizing

    def plot_average_salaries(self):
        self.print_separator()
        mean1 = self.df.groupby('Year')['TotalPayBenefits'].mean()
        mean2 = self.sub_df.groupby('Department')['TotalPayBenefits'].mean()
        mean3 = self.sub_df.groupby('Year')['TotalPayBenefits'].mean()
        mean4 = self.sub_df.groupby(['Department','Year'])['TotalPayBenefits'].mean()
        plt.figure()
        plt.suptitle("Average_Salary_Comparison",fontsize = 20)
        plt.subplot(3,2,1)
        mean1.plot(kind='bar')
        plt.title('Average_Salaries per year')
        plt.ylabel('Average_Salaries')
        plt.xticks(rotation=0)
        plt.subplot(3,2,2)
        mean2.plot(kind='bar')
        plt.title('Average_Salaries per Departments')
        plt.ylabel('Average_Salaries')
        plt.xticks(rotation=0)
        plt.subplot(3,2,5)
        mean3.plot(kind='bar')
        plt.title('Mean Average_Salaries per Year for Departments')
        plt.ylabel('Average_Salaries')
        plt.xticks(rotation=0)
        plt.subplot(3,2,6)
        a = mean4.plot(kind='bar')
        labels = ['FD_2011', 'FD_2012', 'FD_2013', 'FD_2014', 'PD_2011', 'PD_2012', 'PD_2013', 'PD_2014']
        a.set_xticklabels(labels)
        plt.title('Average_Salaries per Departmebts_Year')
        plt.ylabel('Average_Salaries')
        plt.xticks(rotation=0)
        plt.show()
