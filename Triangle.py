def solution(A):
    # write your code in Python 3.6
    if len(A) < 3:
        return 0
    A.sort()
    for i in range(len(A)-1,2,-1):
        if A[i-1] + A[i-2] > A[i]:
            return 1
    return 0