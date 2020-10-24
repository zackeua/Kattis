word = input()
guesses = input()

winning = 0
temp = 0
for guess in guesses:
        if guess not in word:
                temp += 1
        else:
                winning += temp
                temp = 0

print('WIN' if winning < 10 else 'LOSE')