#python program intersection in dictionaries

ini_dict1 = {'a': 1, 'b' : 5, 'c' : 10, 'd' : 15}
ini_dict2 = {'a' :1, 'c' : 10, 'd' : 56}

final_dict = {x:ini_dict1[x] for x in ini_dict1 if x in ini_dict2}
print ("Final Dictionary: ", str(final_dict))