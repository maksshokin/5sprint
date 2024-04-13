import sys, string  #111848667 111849224


def decoder(phrase: str)-> str:
    """Без рекурсии"""
    stack: list[tuple] = []
    numbers: str = ''
    result: str = ''
    for letter in phrase:
        match letter:
            case '[':
                stack.append((result, numbers))
                numbers = result = ''
            case ']':
                past_result, past_numbers = stack.pop()
                result = past_result + result * int(past_numbers)
            case _:
                if letter in string.digits:
                    numbers += letter
                else:
                    result += letter
    return result

if __name__ == '__main__':
    print(decoder(sys.stdin.readline().rstrip()))  