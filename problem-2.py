# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

#Brute fore
# def two_sum(arr,target) -> bool:
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i]+arr[j] == target: 
#                 return True
#     return False

#Hashmap
def two_sum(arr,target) -> bool:
    hashmap = {}
    for idx in range(len(arr)):
        diff = target - arr[idx]
        if diff in hashmap:
            return True
        hashmap[arr[idx]] = diff
    return False        


if __name__ == "__main__":
    assert two_sum([10, 15, 3, 7],17)
    print("Test case passed")

