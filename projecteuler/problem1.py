num_range = range(1,1000)
multiples  = []

[multiples.append(i) for i in num_range if i % 3 == 0 or i % 5 == 0]
        
total = sum(multiples)

print total