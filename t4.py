s = {'one':1,'two':2,'three':3}
print(s)
m = iter(s)  # !!!
try:
    while True:
        print(m.next())  # s[m.next()]
except StopIteration:
    pass