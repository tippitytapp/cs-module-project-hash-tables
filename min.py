data = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

# all all the smallest comments
total = 0
for index, value in enumerate(data):
    smallest = min(value)
    total += smallest
    print(min(value))
print(total)            
