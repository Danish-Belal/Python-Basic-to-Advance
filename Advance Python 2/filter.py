# filter create a list of item for which the function return true.

def NoGreaterthen5(num):
    if num>5:
        return True
    else:
        return False  

l = [1,3,4,6,7,9,79,6,8,6798,67,865,]  

lfun = lambda num:num>5
print(list(filter(lfun , l)))   # fun can be lamda function also


#print(list(filter(NoGreaterthen5 , l)))
a=(list(filter(NoGreaterthen5 , l)))   # it takes function and input list and then filter list for true value form function.

print(a)
print(sorted(a))  # sorted(a) will print sorted list in assending order.

