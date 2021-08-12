# Reduce applies a rolling computation to sequential pair of element.

# to use reduce we need to import reduct from functool
from functools import reduce


sum = lambda a , b : a+b

l = [1, 2, 3, 4]
val = reduce(sum , l)
print(val)

# Sequential computatoion is , first 1 will add with 2 , then sum 3 will add with 3 , then value return from sun 6 will add with 4 and finally return 10.





