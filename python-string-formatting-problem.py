def print_formatted(number):
    # your code goes here
    n=number
    width = len('{:b}'.format(n))+1
    for i in range(1,n+1):
        print(str.rjust(str(i), width-1)+str.rjust('{:o}'.format(i), width)+str.rjust('{:X}'.format(i), width)+str.rjust('{:b}'.format(i), width))

#rjust returns a new string of given length after substituing in the left side of the original string
#string.rjust(string,length)

#ljust works by returning a string of given length after substitution in the
#right side of the string.


