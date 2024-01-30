import numpy as np

class DataCleaner:
    def __init__(self, df):
        self.df = df

    def print_separator(self):
        print("#################################################\n")

# Checks if there any negative values in the dataframe

    def print_negative_values(self):
        self.print_separator()
        print("\n ######### {data before cleaning} #########\n")
        print("Negative values : \n")
        for col in self.df.select_dtypes(include=[np.number]).columns:
            if (self.df[col] < 0).any():
                print(f"Column '{col} :  T")
            else:
                print(f"Column '{col} :  F")

# Checks if there any null values in the dataframe

    def print_null_values(self):
        self.print_separator()
        print("NUll values : \n")
        for col in self.df.columns:
            if self.df[col].isnull().any():
                print(f"Column '{col} :  T")
            else:
                print(f"Column '{col} :  F")

# Cleans the dataframe

    def clean_data(self):
        for col in self.df.select_dtypes(include=[np.number]).columns:
            self.df[col] = self.df[col].clip(lower=0)
        self.df.fillna(0, inplace=True)
        self.df = self.df.drop('Notes', axis=1)
        self.df = self.df.drop('Status', axis=1)
        self.df = self.df.drop('EmployeeName',axis=1)
        return self.df
    def print_cleaned_data(self):
        self.print_separator()
        print("\n######### {data after cleaning} #########\n")
        print("Negative_Values : \n")
        for col in self.df.select_dtypes(include=[np.number]).columns:
            if (self.df[col] < 0).any():
                print(f"Column '{col} :  T")
            else:
                print(f"Column '{col} :  F")
        self.print_separator()
        print("NUll_Values : \n")
        for col in self.df.columns:
            if self.df[col].isnull().any():
                print(f"Column '{col} : T")
            else:
                print(f"Column '{col} : F")
        df=self.df
        return df

# Checks if the the numeric cols is right_Calculated

    def check_calculations(self):
        self.print_separator()
        mask1 = self.df['TotalPay'] == self.df['BasePay'] + self.df['OvertimePay'] + self.df['OtherPay']
        if mask1.all:
            print("[TotalPay] is right_calculated\n ")
        else:
            print("[TotalPay] isnt right_calculated\n ")
        mask2 = ((self.df['TotalPayBenefits'] == self.df['TotalPay'] + self.df['Benefits']) & (self.df['TotalPayBenefits'] == self.df['BasePay'] + self.df['OvertimePay'] + self.df['OtherPay'] + self.df['Benefits']))
        if mask2.all:
            print("[TotalPayBenefits] is right_calculated\n")
        else:
            print("[TotalPayBenefits] isnt right_calculated\n")
        
