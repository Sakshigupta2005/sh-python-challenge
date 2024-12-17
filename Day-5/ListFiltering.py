#python prohram of List Filtering

def odd(x):
 return x % 2 == 1
def even(x):
 return x % 2 != 1
a = [2, 5, 7, 8, 10, 13, 16]
odd_result = filter(odd, a)
even_result = filter(even, a)
print('Original List :', a)
print('Filtered List :', list(odd_result))
print('Filtered List :', list(even_result))