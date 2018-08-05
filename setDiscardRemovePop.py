n = int(input())
s = set(map(int, input().split()))
test = int(input())
for tes in range(test):
    command = str(input())
    tem = command[:].split()
    if tem[0]=='discard':
        s.discard(int(tem[1]))
    elif tem[0]=='pop':
        if len(s)>0:
            s.pop()        
    else:
        if len(s)>0:
            s.remove(int(tem[1]))
    

sumi =0
for nu in s:
    sumi += nu
print(sumi)
