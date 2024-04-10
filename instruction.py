import sys

def printer(times, capacity):
    return capacity * times

instruction: str = sys.stdin.readline().rstrip()

def number_of_times(phrase: str)-> int:
    """Возвращает целое число"""
    times: str = ''
    times_check = True
    for symbol in phrase:
        if times_check:
            try:
                times += str(int(symbol))
            except ValueError:
                if symbol == '[':
                    times_check = False
                pass
    if len(times) > 0:
        return int(times)
    else:
        return 1

def starter(phrase):
    """Удаляет все, кроме незашифроманного начала"""
    clear_phrase = ''
    for symbol in phrase:
        try:
            check = int(symbol)
            break
        except ValueError:
            clear_phrase += symbol
    return clear_phrase

def opener(phrase, times=1):
    """Рекурсиная открывашка для символов внутри []"""
    check = False
    symbols = ''
    count = 0
    for i in range(len(phrase)):
        if phrase[i] == ']':
            count -= 1
            if count == 0:
                check = False
                break
        if check:
            symbols += phrase[i]
        if phrase[i] == '[':
            count += 1
            check = True
    
    if '[' in symbols:
        return (starter(symbols) + opener(symbols, number_of_times(symbols))) * times
    else:
        return symbols * times

def connecting(prhase):
    result = starter(prhase) + opener(prhase, number_of_times(prhase))

    return 



print(connecting(instruction))