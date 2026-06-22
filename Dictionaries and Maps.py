# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n = int(input())
phone_book = {}

# Read n entries into dictionary
for _ in range(n):
    name, number = input().split()
    phone_book[name] = number

# Read queries until EOF
for line in sys.stdin:
    name = line.strip()
    if name in phone_book:
        print(f"{name}={phone_book[name]}")
    else:
        print("Not found")
