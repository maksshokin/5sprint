import sys

people = [int(number)+1 for number in range(int(sys.stdin.readline().rstrip()))]
tact: int = int(sys.stdin.readline().rstrip())
 
while len(people) > 1:
    if len(people) >= tact:
        people.pop(tact-1)
    #else:
        
print(people[0])