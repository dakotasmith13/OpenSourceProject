# initialize variables
a, b = 0, 1
sum_even = 0

# determine if b is even
while b < 4000000:
    if b % 2 == 0:
        sum_even += b
    # set a = b and b to the sum of a + b
    a, b = b, a+b

# display value of sum of even numbers
print(sum_even)

# answer should be 4613732
