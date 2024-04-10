import sys
import re
import collections


instruction: str = sys.stdin.readline().rstrip()
numbers = collections.deque([int(number) for number in re.findall(r'\d+', instruction)])

string = instruction
delimiters = ["]", "[", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for delimiter in delimiters:
    string = " ".join(string.split(delimiter))
letters = collections.deque(string.split())

print(numbers, letters)
print(instruction.index('['))
print(instruction.index(']'))

unencrypted = ''
if instruction.index(numbers[0]) > 0:
    unencrypted += letters[0]
    letters.leftpop()

def translator(phrase, numbers, letters):
    
    count = 0
    check = False
    inside_part = ''
    for symbol in phrase:
        if symbol == '[':
            count += 1
            check = True
        if check:
            inside_part += symbol
        if symbol == ']':
            count -= 1
    if '[' or ']' in symbols:
        return  + opener(symbols, number_of_times(symbols))) * times
    else:
        return symbols * times

        
