def odd_range(arr):
    result = []

    for num in arr:
        result.append(num % 3)
    
    return result

print(odd_range([1, 3, 5, 7, 9, 11, 13]))
print(odd_range([1, 3, 5 ]))