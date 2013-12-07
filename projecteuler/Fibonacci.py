fib_list = []
lidt = [0,1]


def fib(n):
    if n < 2:
        print n
    else:
        i = 2
        while i < n :
            fib_num =  (lidt[1-1])+(lidt[1-2])
            lidt.append(fib_num)
            i += 1
            return lidt
        
n = raw_input('What is your range? ')
fib(n)