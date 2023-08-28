# d = {'hh': [0,2,5,[{'abc':['soundar',{kk: [c:'g']}]}]]}
d  = [{'test': 'jjjjjj', 'ff': [1,2,3,5,'soundar', {'jj': [1,2,3,4,['fff', {'ff': 'ttttttt'}]]}]}]

#print(d[0]['ff'][4])

#print(d[0]['ff'][5]['jj'][4][1]['ff'])

for i in range(len(d)):
    print(d[i]['ff'])
    l = d[i]['ff']
    print(len(l))