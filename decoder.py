import sys  #10 апр 2024, 23:29:52 ID 111789751


instruction: str = sys.stdin.readline().rstrip()

def decoder(phrase: str)-> str:
    """Функция, расшивровывающая послания"""
    result: str = ''  
    message: str = ''  #промежуточная переменная для хранения символов
    numbers: str = ''
    count: int = 0  #считает глубину вложенности 0[1[2[3]]]
    counter: int = 0  #считает длину промежуточной переменной
    for letter in phrase:
        counter += 1
        if count == 0:
            if not letter == '[':
                try:
                    numbers += str(int(letter))
                except ValueError:
                    message += letter
                    if counter == len(phrase):
                        result += message
                        message = ''
            else:
                times = int(numbers)
                numbers = ''
                result += message
                message = ''
                count += 1
        else:
            if letter == '[':
                count += 1
            if letter == ']':
                count -= 1
            if not count == 0:
                message += letter
            if count == 0:
                result += decoder(message)*times
                message = ''   
    return result
print(decoder(instruction))