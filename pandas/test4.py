import pandas as pd

client = {
    'id': [1,2,3],
    'name' : ['x','y','z']
}

command = {
    'ireder_id': [100, 200,250],
    'id' : [1,2,1],
    'amount': [300, 140,500]
}

merge = pd.merge(client, command, on='id')
print(merge)