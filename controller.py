import data
from view import input_data, view_data

def btm ():
    num_data = [input_data('Введите фамилию '), input_data('Введите имя '), input_data('Отчество '), int(input_data('телефон ')), input_data('заметки ') ]
    data.init_data(*num_data)
    with open ('book.csv', 'a') as file:
        for i in range (len(num_data)):
            file.writelines (f'{num_data[i]} ')
        file.write('\n')
    view_data (num_data)


