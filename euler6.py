## Sum square differnce

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

n = 100
s1 = 0
s2 = 0
for i in range(1, n+1):
    s1 = i*i + s1
    s2 = s2 + i
answer = s2 * s2 - s1
print(s1)
print(s2*s2)
print('the answer for Euler 6 is: ', answer)
