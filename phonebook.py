# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


number = int(sys.stdin.readline())
dict={}
for i in range(number):
    line= sys.stdin.readline().strip()
    line= line.split(" ")
    dict[line[0]]=line[1]

for i in range(number):
    name= sys.stdin.readline().strip()
    if name in dict:
        print(name+"="+dict[name])
    else:
        print("Not found")
        
# read input.txt and pass to to above code and check output.txt
# python phonebook.py < input.txt > output.txt
    
