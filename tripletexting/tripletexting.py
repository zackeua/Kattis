text = input()
l = len(text)//3

[print(text[i] if text[i] == text[i+l] else text[i+2*l], end='') for i in range(l)]
