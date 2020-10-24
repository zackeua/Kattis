
letter = {'clank':'a', 'bong':'b', 'click':'c',
'tap':'d', 'poing':'e', 'clonk':'f', 'clack':'g',
'ping':'h', 'tip':'i', 'cloing':'j', 'tic':'k',
'cling':'l', 'bing':'m', 'pong':'n', 'clang':'o',
'pang':'p', 'clong':'q', 'tac':'r', 'boing':'s',
'boink':'t', 'cloink':'u', 'rattle':'v', 'clock':'w',
'toc':'x', 'clink':'y', 'tuc':'z',
'whack':' ', 'bump':'caps', 'pop':'delete',
'dink':'shift_down', 'thumb':'shift_up'}

s = ''
caps = False
shift = False

n = int(input())
i = 0
while i < n:
    inn = input()
    l = letter[inn]
    if l == 'caps':
        caps = not caps
    elif l == 'delete':
        s = s[:-1]
    elif l == 'shift_up':
        shift = False
    elif l == 'shift_down':
        shift = True
    else:
        if caps ^ shift: # xor
            s = s + l.upper()
        else:
            s = s + l
    i += 1

print(s)
