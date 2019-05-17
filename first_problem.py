""" Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def mul_arr(arr):
    mul = 1
    sol = []
    for i in arr:
        mul = mul * i
    for i in range(len(arr)):
        sol.append(int(mul / arr[i]))
    print(sol)

def mul_arr_without_division(arr):
    sol = [0 for i in range(len(arr))]
    mul_sx_to_dx = [1 for _ in range(len(arr))]
    mul_dx_to_sx = [1 for _ in range(len(arr))]
    mul = 1
    for i in range(len(arr)):
        mul_sx_to_dx[i] = arr[i] * mul
        mul = mul_sx_to_dx[i]
    mul = 1
    for i in range(len(arr)-1,-1,-1):
        mul_dx_to_sx[i] = arr[i] * mul
        mul = mul_dx_to_sx[i]
    for i in range(0,len(arr)):
        if(i==0):
            sol[i] = mul_dx_to_sx[i+1]
        elif(i==len(arr)-1):
            sol[i] = mul_sx_to_dx[i-1]
        else:
            sol[i] = mul_sx_to_dx[i-1] * mul_dx_to_sx[i+1]
    print(sol)


if __name__=="__main__":
    arr = [4,2,1]
    mul_arr_without_division(arr)
