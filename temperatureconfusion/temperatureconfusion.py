
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

data = input()
a, b = list(map(int,data.split("/")))

# a_f/b_f = 9/5 * a_c/b_c +32

# (a_f-32*b_f)*5/b_f*9 = * a_c/b_c

top = (a-32*b)*5
bottom = b*9

factor = gcd(top,bottom)

top = top//factor
bottom = bottom//factor


print(f'{top}/{bottom}')
