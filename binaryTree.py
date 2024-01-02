# which branch is larger

def count_left(loop, arr, i, left):
    for num in range(loop):
        if i >= len(arr): return left,i
        left += arr[i]
        i += 1
    return left,i

def count_right(loop, arr, i, right):
    for num in range(loop):
        if i >= len(arr): return right,i
        right += arr[i]
        i += 1
    return right,i

def solution(arr):
    # Type your solution here 
    left = 0
    loop = 1
    right = 0
    i = 1
    
    if len(arr) == 0: return ""
    while i < len(arr):
        left, i = count_left(loop, arr, i, left)
        right, i = count_right(loop, arr, i, right)
        loop = loop * 2
    
    if right > left: return "Right"
    if left > right: return "Left"
    if left == right: return ""
    
    
    pass