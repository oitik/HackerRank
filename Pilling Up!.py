def solve(data):
    n = data[0]
    lis = data[1]
    stk = [10000000000]
    left = 0
    right = n-1
    for i in range(n):
        if lis[left] >= lis[right]:
            stk.append(lis[left])
            if stk[i+1] > stk[i]:
                return 'No'
            left += 1
        elif lis[left] < lis[right]:
            stk.append(lis[right])
            if stk[i+1] > stk[i]:
                return 'No'
            right -= 1
    return 'Yes'


t = int(input())
in_list = []
for i in range(t):
    n = int(input())
    x = [int(x) for x in input().split()]
    x = (n, x)
    in_list.append(x)
for val in in_list:
    print(solve(val))

