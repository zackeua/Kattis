text = input()

chars = {}
print1= True
for c in text:
        if c in chars:
                print1 = False
                break
        else:
                chars[c] = 1
print(1 if print1 else 0)