num = list(map(int,input().split()))

s = (num[0]+num[1]+num[2]+num[3])/2

print(((s-num[0])*(s-num[1])*(s-num[2])*(s-num[3]))**(1/2))
