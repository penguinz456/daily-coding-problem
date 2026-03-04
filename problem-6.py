# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.

 # Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

def is_palindrome(x : int) -> bool:
    if x < 0 or (x%10 == 0 and x != 0):
        return False
    if x < 10: 
        return True
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half*10 + x%10
        x//=10
    return x == reversed_half or x == reversed_half // 10
    
if __name__ == "__main__":
    # ===== Basic cases =====
    assert is_palindrome(121) == True
    assert is_palindrome(-121) == False
    assert is_palindrome(10) == False

    # ===== Single digit =====
    assert is_palindrome(0) == True
    assert is_palindrome(7) == True
    assert is_palindrome(-7) == False

    # ===== Even length =====
    assert is_palindrome(1221) == True
    assert is_palindrome(1001) == True

    # ===== Odd length =====
    assert is_palindrome(12321) == True
    assert is_palindrome(12331) == False

    # ===== Numbers ending with zero =====
    assert is_palindrome(100) == False
    assert is_palindrome(10001) == True

    # ===== Large numbers =====
    assert is_palindrome(123454321) == True
    assert is_palindrome(123456789) == False

    # ===== Edge integer cases =====
    assert is_palindrome(2147447412) == True
    assert is_palindrome(2147483647) == False  # max 32-bit int

    print("All test cases passed!")