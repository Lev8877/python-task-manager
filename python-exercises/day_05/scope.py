counter = 0
#Параметр 
def increase_counter(counter = 0):
    return counter + 1

#Глобальная переменная 
counter = 0
def increase_counter():
    global counter 
    counter += 1
