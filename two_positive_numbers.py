def two_positive(a, b, c):
    positive_count = 0
    
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    
    return positive_count == 2

# Test cases
print(two_positive(1, -2, 3))  
print(two_positive(-1, 2, 0))
print(two_positive(0, 0, 0))
print(two_positive(-1, -2, -3)) 
