import pandas as pd
import scipy as sp
from scipy import stats

# import the data

jama_data = pd.read_table('https://ww2.amstat.org/publications/jse/datasets/normtemp.dat.txt', 
                          sep="   ", 
                          engine='python',
                          header=None,
                          names = ["body_temp", "sex", "heart_rate"])

mu = 98.6

print('')
print('the t-statistic is %6.9f and the p-value = %6.9f' %  stats.ttest_1samp(jama_data['body_temp'], mu))
print('')
print('We reject the null hypothesis. The true population mean of human body temperature is not 98.6 F. ')
print('')