# --------------
# Importing header files
import numpy as np
import warnings
import statistics
from statistics import stdev
warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census = np.concatenate((new_record,data),axis=0)
age = census[:,0]
max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = stdev(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==0]
race_2=census[census[:,2]==0]
race_3=census[census[:,2]==0]
race_4=census[census[:,2]==0]
len_0= len(race_0)
len_1= len(race_1)
len_2= len(race_2)
len_3= len(race_3)
len_4= len(race_4)
minority_race= min(len_0,len_1,len_2,len_3,len_4)
print(minority_race)
senior_citizens= census[age>60]
senior_citizens_len=len(senior_citizens)
working_hours_sum=senior_citizens.sum(axis=0)[6]
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=statistics.mean(high[:,7])
avg_pay_low=statistics.mean(low[:,7])
print(avg_pay_high)
print(avg_pay_low)



