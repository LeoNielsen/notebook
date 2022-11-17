import numpy as np
import matplotlib.pyplot as plt

file_name = "notebooks/data/befkbhalderstatkode.csv"
neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
          5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
          10: 'Amager Vest', 99: 'Udenfor'}
data = np.genfromtxt(file_name , delimiter=',',dtype=np.uint, skip_header=1)

pll_in_each_neighb = {}

for x in neighb:
    pll_in_each_neighb[neighb[x]] = np.sum(data[(data[:,0] == 2015) & (data[:,1] == x)][:,-1])

pll_in_each_neighb = dict(sorted(pll_in_each_neighb.items(), key=lambda item: item[1]))

plt.bar(pll_in_each_neighb.keys(),pll_in_each_neighb.values(), width=0.5)
plt.show()

above_65 = data[(data[:,0] == 2015) & (data[:,2] > 65)]
#print("above 65: ", sum(above_65[:,-1]))

above_65_not_danish = above_65[above_65[:,3] != 5100]
#print("not danish above 65", sum(above_65_not_danish[:,-1]))

a = {}
for x in range(1992,2016):
    a[x] = sum(data[(data[:,0] == x) & ((data[:,1] == 2) | (data[:,1] == 4))][:,-1])

#plt.plot(a.keys(), a.values())
#plt.show()
