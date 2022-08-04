def init_data (a,b,c,d,e):
    global surname_data, name_data, second_name_data, phone_data, note_data 
    surname_data = a
    name_data = b
    second_name_data = c
    phone_data = d
    note_data = e

def return_data ():
    global surname_data, name_data, second_name_data, phone_data, note_data 
    return surname_data, name_data, second_name_data, phone_data, note_data 

