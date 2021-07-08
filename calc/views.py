from django.shortcuts import render

num1 = 0
com = ''
num2 = 0
sum = 0
def calc(request):
    sum = num1 + num2
    return render(request, 'index.html', {'num1': num1, 'com': com, 'num2':num2, 'sum': sum})

def main_Calc(request, number1, command, number2):
    num1 = number1
    num2 = number2
    com = command
    if com == '+':
        sum = num1 + num2
    elif com == '-':
        sum = num1 - num2
    elif com == '*':
        sum = num1 * num2
    elif com == 'div':
        com = '/'
        if num2 != 0:
            sum = num1 / num2
        else:
            return render(request, 'index.html', {'num1': num1, 'com': com, 'num2': num2, 'sum': 'error'})
    elif com == '**':
        sum = num1 ** num2
    return render(request, 'index.html', {'num1': num1, 'com': com, 'num2':num2, 'sum': sum})