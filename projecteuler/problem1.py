num_range = range(1,1000)
total = 0
multiples  = []

for i in num_range:
    if i % 3 == 0 or i % 5 == 0:
        multiples.append(i)
        
total = sum(multiples)

print total