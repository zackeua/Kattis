N = int(input())
i = 0
time = 0
while i < N:
    if i%2==0:
        num1 = int(input())
    else:
        num2 = int(input())
        time += num2-num1
    i += 1

if N%2 != 0:
    print("still running")
else:
    print(time)
