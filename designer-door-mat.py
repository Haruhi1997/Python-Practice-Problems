N,M = map(int,input().split())

pattern = [('.|.'*(2*i+1)).center(M,'-') for i in range(N//2)]

print('\n'.join(pattern+['WELCOME'.center(M,'-')]+pattern[::-1]))

#Here str.center(width,fillcharacter) makes the str string in the center of a st#ring of width = 'width' and fills the remaning length of the string with the fil#l character
