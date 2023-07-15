# poisson distribution with parameter(lam) = +2 and size of returned array(size) = 1000

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

dist0=random.poisson(lam=2,size=1000)
dist1=random.poisson(lam=2)

sns.distplot(dist0)
plt.show()