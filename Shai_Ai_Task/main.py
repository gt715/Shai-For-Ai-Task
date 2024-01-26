import pandas as pd
import os
from data_explorer import DataExplorer
from data_statistics import DataStatistics
from data_cleaner import DataCleaner
from data_visualizer import DataVisualizer
from data_analyzer import DataAnalyzer
from data_correlation import DataCorrelation
os.system('cls')




# Load the data
df = pd.read_csv('C:\Games\DB project\Shai_Ai_Task\Salaries.csv')#dont forget to change the path of the dataframe
sub_df = df[df['JobTitle'].str.contains('Department', case=False)].copy()


# Create an instance of DataExplorer and call its methods
explorer = DataExplorer(df)
explorer.show_info()
explorer.show_shape()
explorer.show_dtypes()
explorer.show_null_cols()
explorer.show_null_counts()

# Create an instance of DataCleaner and call its methods
cleaner = DataCleaner(df)
cleaner.print_negative_values()
cleaner.print_null_values()
df=cleaner.clean_data()
cleaner.print_cleaned_data()
cleaner.check_calculations()

# Create an instance of DataStatistics and call its methods
stats = DataStatistics(df)
stats.show_stats()
stats.modes(1)



# Create an instance of DataVisualizer and call its methods
visualizer = DataVisualizer(df,sub_df)
visualizer.plot_salary_distribution()
visualizer.plot_job_title_distribution()
sub_df=visualizer.plot_department_distribution()


# Create an instance of DataAnalyzer and call its methods
analyzer = DataAnalyzer(df, sub_df)
analyzer.group_by_year()
analyzer.group_by_department()
analyzer.group_by_department_year()
analyzer.calculate_average_salary()
analyzer.plot_average_salaries()

# Create an instance of DataCorrelation and call its methods
correlation = DataCorrelation(df)
correlation.calculate_and_visualize_correlation()
