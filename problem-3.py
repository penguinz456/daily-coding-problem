# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

#naive approach 
# def product_of_Array(arr)->list[int]:
#     product = 1
#     result = [0]*len(arr)
#     count_zero = 0
#     flag = 0
#     for i in range(len(arr)):
#         if arr[i] == 0: 
#             count_zero += 1 
#             flag = i
#             print(i)
#         else:
#             product*=arr[i]
#     if count_zero > 1: 
#             return result
#     if count_zero == 1:
#             result[flag] = product
#             return result
#     for i in range(len(arr)):
#         result[i] = product//arr[i]
#     return result


###no division
def product_of_Array(arr) -> list[int]:
    n = len(arr)
    result = [1]*n
    prod_left = 1
    prod_right = 1
    for i in range(n):
       result[i] = prod_left
       prod_left *= arr[i]
    for i in range(n-1,-1, -1):
        result[i] *= prod_right
        prod_right *= arr[i]
       
    return result   

print(product_of_Array([1,2,3,4,5]))


# [1, 1, 2, 6, 24]
# [120,60,20,5,1]