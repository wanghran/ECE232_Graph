import pandas as pd
import numpy as np
import os
import re
import matplotlib.pyplot as plt
dir = '../data/data/'

def to_time_series(csv_name):
    df = pd.read_csv(dir+csv_name)
    df.Date = pd.to_datetime(df.Date)
    time_series = pd.Series(df.Close.values, index=df.Date)
    return time_series

def to_r_i(csv_name):
    p_i_t = to_time_series(csv_name)
    p_i_t_1 = p_i_t.shift(1)
    q_i_t = (p_i_t-p_i_t_1)/p_i_t_1
    r_i = np.log(1+q_i_t)
    return r_i.iloc[1:]

def get_correlation(csv_name_i, csv_name_j):
    r_i = to_r_i(csv_name_i)
    r_j = to_r_i(csv_name_j)
    numerator = np.mean(r_i*r_j) - np.mean(r_i)*np.mean(r_j)
    denominator = np.sqrt((np.mean(np.square(r_i)) - np.square(np.mean(r_i)))*(np.mean(np.square(r_j)) - np.square(np.mean(r_j))))
    return numerator / denominator

def get_weight(csv_name_i, csv_name_j):
    p_ij = get_correlation(csv_name_i, csv_name_j)
    return np.sqrt(2*(1-p_ij))


stock_files = os.listdir(dir)
weights = []
with open('../output/stock_edgelist.txt', 'w+') as f:
    for i in range(len(stock_files)):
        for j in range(len(stock_files)):
            csv_name_i = stock_files[i]
            csv_name_j = stock_files[j]
            if csv_name_i == csv_name_j:
                continue
            if csv_name_i == '.DS_Store' or csv_name_j == '.DS_Store':
                continue
            w_ij = get_weight(csv_name_i,csv_name_j)
            ticker_i = re.sub(r'\.csv$', '', csv_name_i)
            ticker_j = re.sub(r'\.csv$', '', csv_name_j)
            weights.append(w_ij)
            f.write("%s\t%s\t%f\n"%(ticker_i, ticker_j, w_ij))
        print(i)

plt.hist(weights, bins='auto')  # arguments are passed to np.histogram
plt.title("Weight Distribution of Correlation")
plt.show()


