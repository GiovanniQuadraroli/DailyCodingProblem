#There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
# Given N, write a function that returns the number of unique ways you can climb the staircase. 
# The order of the steps matters.
#For example, if N is 4, then there are 5 unique ways:
#    1, 1, 1, 1
#    2, 1, 1
#    1, 2, 1
#    1, 1, 2
#    2, 2


#We can find the solution with dynamic programming. Let's see the unique ways for the example with 
# N = 4 and for the unique ways for a staircase with 3 steps and for a staircase with 2 steps:
#  N = 4            N = 3       N = 2
# 1) 1,1,1,1        1,1,1       1,1
# 2) 2,1,1          2,1         2
# 3) 1,2,1          1,2
# 4) 1,1,2
# 5) 2,2

# As you can see when N = 4 the ways to climb the staircase are equal to the ways to climb the staircase with 3 steps adding 1 to the solution
# plus the ways to climb the staircase with 2 steps adding 2 to the solution. So the solution for n = 4 can be written as:
# 1) T[3][1] + "1" = 1,1,1 + "1"
# 2) T[3][2] + "1" = 2,1 + "1"
# 3) T[3][3] + "1" = 1,2 + "1"
# 4) T[2][1] + "2" = 1,1 + "2"
# 5) T[2][2] + "2" = 2 + "2"
# So T[n] = T[n-1] + T[n-2]

# Generally if you have X ways to climb the staircase the solution will be:
# foreach element in X:
# T[n] += T[n - element]


def stairs(n,ways):
    index = 0
    sol = [0 for _ in range(n)]
    for i in range(n):
        if index == 0:
            if ways[index] == i :
                sol[i] = 1
                index += 1
        else:
            if index < len(ways) and ways[index] == i:
                sol[i] = 1
                index += 1
            for x in range(index):
                sol[i] += sol[i - ways[x]]
    print(sol)
    return sol[n-1]


if __name__=="__main__":
    ways = [1,2,5]
    n = 6
    print(stairs(n,ways))


