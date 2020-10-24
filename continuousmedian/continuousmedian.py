T = int(input())
c = 0


while c < T:
    N = int(input())
    nums = list(map(int,input().split()))
    continous_median = 0
    res = 0
    #l = []
    for i in range(N):
        l = nums[:i+1]
        #l = l + [nums[i]]
        l.sort()
        if i%2 == 0:
            res += l[i//2]
        else:
            res += (l[i//2]+l[i//2 + 1])//2
    print(res)
    c+= 1
