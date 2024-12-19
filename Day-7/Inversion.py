#python program Inversion dictionary

def invert_dictionary(original_dict):
 inverted_dict = {value: key for key, value in original_dict.items()}
 return inverted_dict
original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = invert_dictionary(original_dict)
print(inverted_dict) # Output: {1: 'a', 2: 'b', 3: 'c'}