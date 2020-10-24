def order(l):
        order = -1
        for i in range(len(l)-1):
                if order == -1:
                        if l[i] <= l[i+1]:
                                order = 1
                        elif l[i] >= l[i+1]:
                                order = 2
                else:
                        if l[i] <= l[i+1] and order == 1:
                                pass
                        elif l[i] >= l[i+1] and order == 2:
                                pass
                        else:
                                return 'NEITHER'
        if order == 1:
                return 'INCREASING'
        else:
                return 'DECREASING'


N = int(input())
i = 0
names = []
while i < N:
        names.append(input())
        i += 1
print(order(names))