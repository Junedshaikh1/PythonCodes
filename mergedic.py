#Merge two dictionaries into one.
dict1 = {'Juned': 85, 'Samarth': 92, 'Onkar': 78}
dict2 = {'Atipra': 95, 'Ram': 88}
dict3= {**dict1, **dict2}
print("Merged Dictionary: ")
print(merged_dict)
