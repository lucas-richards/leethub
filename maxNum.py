# find the max number from an array of numbers
def solution(numbers):
    numMax = 0
    if len(numbers)!= 0:
        for num in numbers:
            if num > numMax:
                numMax = num
    return numMax
    pass