def merge_the_tools(string, k):
    # your code goes here
    print('\n'.join([''.join(sorted(set(string[i:i+k]), key=string[i:i+k].index)) for i in range(0, len(string), k)]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)