# we can rise our own exception and Error massage.
def increment(num):
    try:
        return int(num)+1

    except:
        raise ValueError(f"Please enter a Integer for increment.")


a = increment(45)
print(a)
b = increment('dgcnf')   # this will rise  Error .
print(b)
