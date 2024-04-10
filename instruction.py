import sys

def printer(times, capacity):
    return capacity * times

instruction: str = sys.stdin.readline().rstrip()

phrase = []
def number_of_times(phrase: str)-> int:
    """Возвращает целое число"""
    times: str =''
    times_check: bool = True
    for symbol in phrase:
        if times_check:
            try:
                times += str(int(symbol))
            except ValueError:
                times_check = False
    if len(times) > 0:
        return int(times)
    return 1

def opener(phrase):
    check = False
    symbols =''
    count = 0
    second_count = 0
    for i in range(len(phrase)):
        if phrase[i] == ']':
            count -= 1
            if count == 0:
                check = False
                if second_count > 1:
                    opener(symbols)
        if check:
            symbols += phrase[i]
        if phrase[i] == '[':
            count += 1
            second_count += 1
            check = True
    
    print(symbols)
opener(instruction)