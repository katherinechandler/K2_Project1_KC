import pandas as pd
import math

# import the data

jama_data = pd.read_table('https://ww2.amstat.org/publications/jse/datasets/normtemp.dat.txt', 
                          sep="   ", 
                          engine='python',
                          header=None,
                          names = ["body_temp", "sex", "heart_rate"])


# manually calculate the t-statistic for a 1-sample t test

xbar = jama_data['body_temp'].mean()
mu = 98.6
s = jama_data['body_temp'].std()
n = len(jama_data['body_temp'])
dof = (len(jama_data)) -1
t = (xbar - mu)/((s/math.sqrt(n)))

print('')
print('the sample mean is {0:0.2f}'.format(xbar))
print('')
print('the one-sample t(dof = {}) is {}'.format(dof,t))
print('')
print('α (0.0005, dof = 129) is 3.3676 and the p-value is <0.0001')
print('')
print('We reject the null hypothesis. The true population mean of human body temperature is not 98.6 F. ')
print('')