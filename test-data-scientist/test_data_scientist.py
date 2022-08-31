import pandas as pd
import math
import numpy as np
import similaritymeasures
import matplotlib.pyplot as plt
from scipy.spatial.distance import directed_hausdorff

def distance(x1,y1,x2,y2):
    res = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
    return res

#def function(traj1,traj3):#myfunction
#    check = false
#    res=0
#    for i in traj1:
#        for j in traj3:
#            a=distance(i[2],i[1],j[2],j[1])
#            if(a <= h):
#                check = true
#        if(check==true):
#            res+=1
#        check=false
#    return res


tracks = pd.read_csv('traks.csv', delimiter=';')

Filter = tracks[['track','y','x']]

#tra1 = (Filter.loc[tracks['track'] == 1]).values.tolist()
#tra2 = (Filter.loc[tracks['track'] == 2]).values.tolist()
#tra3 = (Filter.loc[tracks['track'] == 3]).values.tolist()
#tra4 = (Filter.loc[tracks['track'] == 4]).values.tolist()

tra10 = Filter.loc[tracks['track'] == 1]
tra10 = tra10[['x','y']]
tra10 = tra10.values.tolist()
lst1 = []
for i in tra10:
        lst1.append((i[0],i[1]))
lst1 = np.array(lst1)

tra11 = Filter.loc[tracks['track'] == 2]
tra11 = tra11[['x','y']]
tra11 = tra11.values.tolist()
lst2 = []
for i in tra11:
        lst2.append((i[0],i[1]))
lst2 = np.array(lst2)

tra12 = Filter.loc[tracks['track'] == 3]
tra12 = tra12[['x','y']]
tra12 = tra12.values.tolist()
lst3 = []
for i in tra12:
        lst3.append((i[0],i[1]))
lst3 = np.array(lst3)

tra13 = Filter.loc[tracks['track'] == 4]
tra13 = tra13[['x','y']]
tra13 = tra13.values.tolist()
lst4 = []
for i in tra13:
        lst4.append((i[0],i[1]))
lst4 = np.array(lst4)

#print(directed_hausdorff(tra10,tra11)[0])

# quantify the difference between the two curves using PCM
pcm = similaritymeasures.pcm(lst1, lst2)

# quantify the difference between the two curves using
# Curve Length based similarity measure
#cl = similaritymeasures.curve_length_measure(lst1, lst2)

# print the results
print("Similar 1 to 2: ", similaritymeasures.pcm(lst1, lst2))
print("Similar 1 to 3: ", similaritymeasures.pcm(lst1, lst3))
print("Similar 1 to 4: ", similaritymeasures.pcm(lst1, lst4))
print("Similar 2 to 4: ", similaritymeasures.pcm(lst2, lst4))
print("Similar 3 to 4: ", similaritymeasures.pcm(lst3, lst4))

#h=150
#print("Result for task 1: ", function(tra1,tra3))
#print("Result for task 2: ", function(tra1,tra2))
#print("4 1: ", function(tra1,tra4)/len(tra1), "4 2: ", function(tra2,tra4)/len(tra2), "4 3: ", function(tra3,tra4)/len(tra3))
