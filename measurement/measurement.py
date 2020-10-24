import sys

l = list(sys.stdin)[0].split()
v = int(l[0])
u = l[1]
u_new = l[3]

thou = 0
if u in ['thou','th']:
    thou = v
elif u in ['inch','in']:
    thou = 1000*v
elif u in ['foot','ft']:
    thou = 12*1000*v
elif u in ['yard','yd']:
    thou = 3*12*1000*v
elif u in ['chain','ch']:
    thou = 22*3*12*1000*v
elif u in ['furlong','fur']:
    thou = 10*22*3*12*1000*v
elif u in ['mile','mi']:
    thou = 8*10*22*3*12*1000*v
else:
    thou = 3*8*10*22*3*12*1000*v
if u_new in ['thou','th']:
    print(thou)
elif u_new in ['inch','in']:
    print(thou/1000)
elif u_new in ['foot','ft']:
    print(thou/(12*1000))
elif u_new in ['yard','yd']:
    print(thou/(3*12*1000))
elif u_new in ['chain','ch']:
    print(thou/(22*3*12*1000))
elif u_new in ['furlong','fur']:
    print(thou/(10*22*3*12*1000))
elif u_new in ['mile','mi']:
    print(thou/(8*10*22*3*12*1000))
else:
    print(thou/(3*8*10*22*3*12*1000))
