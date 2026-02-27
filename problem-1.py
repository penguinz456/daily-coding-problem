# There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.

def climbing_stair(n):
    # a, b = 1,2
    # for i in (n-1):
    #     a,b = b, a+b
    # return a
    if n <= 3: return n
    return climbing_stair(n-1) + climbing_stair(n-2)
    
def climbing_stair_x_steps(n, X) : 
    if n < 0:
        return 0
    if n == 0: 
        return 1
    return sum(climbing_stair_x_steps(n-x,X) for x in X)

if __name__ == "__main__": 
    assert 2 == climbing_stair(2)
    assert 3 == climbing_stair(3)
    assert 5 == climbing_stair(4)
    assert 8 == climbing_stair(5)    
    print("All test case passed")
    ways = climbing_stair_x_steps(5,[1,3,5])
    print(ways)