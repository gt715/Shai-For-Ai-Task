import numpy as np
import statistics



class DataStatistics:
    def __init__(self, df):
        self.df = df
    def print_separator(self):
        print("#################################################\n")

# Calculate the basic statistics of the salary

    def show_stats(self):
        self.print_separator()
        stats = self.df['TotalPayBenefits'].agg(['mean', 'median', statistics.mode, 'min', 'max', 'std', lambda x: x.max() - x.min()]) 
        print(stats)

# Shows the mode you choose and the modes before it

    def modes(self, C):
        self.print_separator()
        values, counts = np.unique(self.df['TotalPayBenefits'], return_counts=True)
        sorted_indices = np.argsort(-counts)
        modes = []
        for i in range(C+1):
            if len(values) > i:
                Mode = values[sorted_indices[i]]
                Mode_Count = counts[sorted_indices[i]]
                modes.append((Mode, Mode_Count))
                print(f"Mode number {i+1} is  : {Mode} , Count: {Mode_Count}\n")
            else:
                print(f"There is no mode number {i+1}\n")
                break
        return modes
