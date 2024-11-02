def result_operation(result: str):
    return print(int(result[result.index(':') + 2:]) + 10)


result_operation('результат операции: 42')
result_operation('результат операции: 54')
result_operation('результат работы программы: 209')
result_operation('результат: 2')
