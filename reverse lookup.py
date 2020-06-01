# INPUTS

data = { "a" : 1 , "b" : 2 , "c" : 3 , "d" : 4 , "e" : 5 }
v_alue = 1

keys = []
for key, value in data.items() :
    if value == v_alue :
        keys.append(key)

print(keys)