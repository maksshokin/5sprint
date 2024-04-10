import sys


instruction: str = sys.stdin.readline().rstrip()

def inc(phrase)-> str:
    result = ''
    mes = ''
    time = ''
    count = 0
    counter = 0
    for letter in phrase:
        counter += 1
        if count == 0:
            if not letter == '[':
                try:
                    time += str(int(letter))
                except ValueError:
                    mes += letter
                    if counter == len(phrase):
                        result += mes 
                        mes = ''
            else:
                times = int(time)
                time = ''
                result += mes
                mes = ''
                count += 1
        else:
            if letter == '[':
                count += 1
            if letter == ']':
                count -= 1
            if not count == 0:
                mes += letter
            if count == 0:
                result += inc(mes)*times   
    return result
print(inc(instruction))