english = set()
french = set()
a = int(input())
a1 = str(input()).split()
b=int(input())
b1 = str(input()).split()
[english.add(i) for i in a1]
[french.add(i) for i in b1]
print(len(english.difference(french)))