n=int(input())
a = set(str(input()).split())
print(a)
test = int(input())
for i in range(test):
    cm = str(input()).split()
    other = set(str(input()).split())
    if cm[0] == 'update':
        a.update(other)
        print(a)
    elif cm[0] == 'intersection_update':
        a.intersection_update(other)
        print(a)
    elif cm[0] == 'difference_update':
        a.difference_update(other)
        print(a)
    elif cm[0] =='symmetric_difference_update':
        a.symmetric_difference_update(other)
        print(a)
su = 0
#[int(j) for j in a]
for t in a:
    su = su+int(t)
print(su)
