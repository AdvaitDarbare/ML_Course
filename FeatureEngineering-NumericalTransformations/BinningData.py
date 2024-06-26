import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn 

coffee = pd.read_csv('starbucks_customers.csv')
ages = coffee['age']

print(np.min(ages))
print(np.max(ages))

age_bins = [12, 20, 30, 40, 71]

coffee['binned_ages'] = pd.cut(ages, age_bins, right = False)

print(coffee['binned_ages'].head(10))

coffee['binned_ages'].value_counts().plot(kind='bar')

plt.show()

