# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for _ in range(t):
    s = input()
    even_chars = s[::2] 
    odd_chars = s[1::2] 
    print(even_chars, odd_chars)
