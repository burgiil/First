# С помощью оператора with читаем документ и результат отмечаем переменной n и закрываем документ. 
with open('names.txt', 'r') as n:
    # Переменной names запишем то, что прочли из переменной n
    names = n.read()
    r = names.split()
    names_out = '\n'.join(r)
    print(names_out)