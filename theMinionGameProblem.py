def minion_game(s):
    # your code goes here
    n = len(s)
    s = s.strip()
    vowels = ['A','E','I','O','U']
    kev = 0
    stu = 0
    for i in range(n):
        if s[i] in vowels:
            kev += n-i
        else:
            stu += n-i
    
    
    if(stu>kev):
        print('Stuart',stu)
    elif(kev>stu):
        print('Kevin',kev)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)