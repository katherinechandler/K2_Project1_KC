import pandas as pd
import math

data = pd.read_table('https://ww2.amstat.org/publications/jse/datasets/normtemp.dat.txt', 
                          sep="   ", 
                          engine='python',
                          header=None,
                          names = ["body_temp", "sex", "heart_rate"])

# this function manually calcuates a one-sample t-statistic and degrees of freedom (DOF) for a user defined value 
# (typically a population mean) and the 1996 JAMA body temperature data set. 
#The function returns a 't-statistic' and DOF for use with a table of critical values. 

def manual_t_calc():
    mu = float(input('What value of body temperature (in F) would you like to compare to the JAMA data?  '))
    xbar = data['body_temp'].mean()
    s = data['body_temp'].std()
    n = len(data['body_temp'])
    dof = (len(data)) -1
    t = (xbar - mu)/((s/math.sqrt(n)))
    print('\nthe sample mean is {0:0.2f}'.format(xbar))
    print('\nthe one-sample t(dof = {}) is {}\n'.format(dof,t))
    
manual_t_calc()
