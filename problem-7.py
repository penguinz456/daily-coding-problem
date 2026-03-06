# 29. Divide Two Integers
# Medium
# Topics
# premium lock icon
# Companies
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

# Constraints:

# -231 <= dividend, divisor <= 231 - 1
# divisor != 0

def divide (dividend:int, divisor:int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if divisor == dividend:
        return 1
    a = abs(dividend)
    b = abs(divisor)
    sign = -1 if (dividend<0) ^ (divisor<0) else 1
    if a < b: return 0
    result = 0
    while a >= b:
        temp = b
        multiple = 1
        while a >= temp << 1:
            temp <<= 1
            multiple<<=1
        a-=temp    
        result+=multiple
    result *= sign
    return min(max(result, INT_MIN), INT_MAX)


if __name__ == "__main__":
    assert divide(10, 3) == 3
    assert divide(7, -3) == -2
    assert divide(-7, 3) == -2
    assert divide(-7, -3) == 2

    # divisible
    assert divide(9, 3) == 3
    assert divide(100, 10) == 10

    # divisor bigger than dividend
    assert divide(3, 5) == 0
    assert divide(-3, 5) == 0

    # divide by 1 and -1
    assert divide(12345, 1) == 12345
    assert divide(12345, -1) == -12345

    # zero dividend
    assert divide(0, 5) == 0

    # edge 32-bit
    assert divide(2147483647, 1) == 2147483647
    assert divide(-2147483648, 1) == -2147483648

    # overflow case
    assert divide(-2147483648, -1) == 2147483647
    print("All tests passed!")
