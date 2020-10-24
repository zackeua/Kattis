R, C = list(map(int, input().split()))
grid = []
words = []
for _ in range(R):
    grid.append(input())

N = list(map(int,input()))[0]

for _ in range(N):
    words.append(input())

for row in range(R-1):
    word_len=0
    for col in range(C-1):
        prev = word_len
        if grid[row][col] == '.' and grid[row][col+1] == '.':
            word_len += 1
        if prev == word_len:
            

print(grid)

print(words)
