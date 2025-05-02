# count all subsets of n
# given an integer n count the number of subsets of that set
# as the number in the set increases, the number of sets doubles
# its basically 2*n
# however returning 2*n would be a bit too easy so lets do a recursive solution
# 2^n can also be defined as 2^n = 2 * 2^(n-1)

def count_all_subsets(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    if n == 0:
        return 1

    return 2 * count_all_subsets(n - 1)
