import pandas as pd
import scipy as sp
from scipy import stats

# import the data

jama_data = pd.read_table('https://ww2.amstat.org/publications/jse/datasets/normtemp.dat.txt', 
                          sep="   ", 
                          engine='python',
                          header=None,
                          names = ["body_temp", "sex", "heart_rate"])

# this function uses the scipy package to calcuate a one-sample t-statistic for a user defined value 
# (typically a population mean) and the 1996 JAMA body temperature data set. 

def scipy_t_calc():
    mu = float(input('What value of body temperature (in F) would you like to compare to the JAMA data?  '))
    print('\nthe t-statistic is %6.9f and the p-value = %6.9f \n' %  stats.ttest_1samp(jama_data['body_temp'], mu))

    
scipy_t_calc()
