import sys


def fibo(grade, number=1):
    if grade <= 1:
        return grade
    else:
        return (fibo(grade-2) + fibo(grade-1))
    
grade: int = int(sys.stdin.readline().rstrip())

print(fibo(grade + 1))