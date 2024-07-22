# С помощью оператора with читаем документ и результат отмечаем переменной n 
with open('names.txt', 'r') as n:
    # Переменной names запишем то, что прочли из переменной n
    names = n.read()
    print(names.splitlines(" "))
    #