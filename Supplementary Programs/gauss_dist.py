# (+2,1) Gaussian Distribution
# 3 methods -- loc (mean)  scale (distribution)  size(x,y) (gives an array of x*y random values; x=number of arrays y=number of elemnts in each array)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

dist0=random.normal(loc=2,scale=1,size=(2,3))
dist1=random.normal(loc=2,scale=1)

print (dist0)
print (dist1)

# plotting the distribution
sns.displot(random.normal(size=10000,loc=2,scale=1), )
plt.show()

