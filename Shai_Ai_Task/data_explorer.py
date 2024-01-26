class DataExplorer:
    def __init__(self, df):
        self.df = df

    def print_separator(self):
        print("#################################################\n")

# Shows general information about the dataframe

    def show_info(self):
        self.print_separator()
        print("\ninfo about the dataframe : \n")
        print(self.df.info())
        print("\n")

# Shows the number of the cols and the rows in the dataframe

    def show_shape(self):
        self.print_separator()
        print("Shape of DataFrame: ", self.df.shape)
        print("\n")

# Shows the datatype of the cols in the dataframe

    def show_dtypes(self):
        self.print_separator()
        print(self.df.dtypes)
        print("\n")

# Shows the cols that have null values(missing values)

    def show_null_cols(self):
        self.print_separator()
        print("the cols that contain empty value : \n")
        print(self.df.isnull().any())
        print("\n")

# Shows the number of null values in each col in the dataframe

    def show_null_counts(self):
        self.print_separator()
        print("number of messing values in each col \n")
        print(self.df.isnull().sum())
        print("\n")
