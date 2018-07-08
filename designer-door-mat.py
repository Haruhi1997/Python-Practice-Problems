
N,M = map(int,input().split())
pattern = [('.|.'*(2*i+1)).center(M,'-') for i in range(N//2)]
print('\n'.join(pattern+['WELCOME'.center(M,'-')]+pattern[::-1]))

#str.center(width,fillcharacter) creates a string of width='width' and places the string=str in the center of the string and fills the remaining width of the string with the fill character.
