# input = [1, 1, 2, 2, 3, 1, 1]
# # Output: [1, 2, 3, 1]

# result=[input[0]] #1

# for i in range(1,len(input)):
#     if input[i]!= input[i-1]:
#         result.append(input[i])

# print(result)        


def max_second_value(tuples):
    max_tuple = tuples[0]  # assume first is max

    for t in tuples[1:]:
        if t[1] > max_tuple[1]:
            max_tuple = t

    return max_tuple

# Test
print(max_second_value([(1, 3), (2, 8), (4, 5)]))  # Output: (2, 8)
