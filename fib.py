# In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1 and F(n) = F(n − 1) + F(n − 2) for n > 1.
# how do we change this recursive call to run in linear time?
# we pass the base case!

def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """

def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """

    def helper(n, prev=1, curr=1):
        if n == 1:
            return prev
        return helper(n - 1, curr, curr + prev)

    return helper(n)

print(find_fibonacci(30))
print(find_fibonacci(50))
