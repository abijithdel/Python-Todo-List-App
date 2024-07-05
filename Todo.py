todo_list = []

def add(value):
    todo_list.append(value)
    print(f'"{value}" Add to To Do List')

def display():
    print('---------------')
    print('Do To LIST')
    print('---------------')
    for index,item in enumerate(todo_list, start=1):
        print(f'{index} - {item}')

def remove(value):
    if value <= len(todo_list):
       print('---------------')
       print(f'Remove "{todo_list[value]}"')
       todo_list.pop(value)
    else:
        print('---------------')
        print(f'Check Input "{value}"')
while True:
    print('###############')
    print('To Do List App')
    print('###############')
    print('1 - Add List')
    print('2 - Display List')
    print('3 - Remove List')
    print('4 - Exit')
    print('###############')


    option = input('Enter Your Option..: ')
    if option == '4':
        break
    elif option in ('1','2','3'):

        if option == '1':
            add_value = input('Enter: ')
            add(add_value)

        if option == '2':
            display() 

        if option == '3':
            display()
            rem_value = int(input('(Remove) Enter Item Number: '))-1
            remove(rem_value)
    else:
        print(f'Oops Option - {option}')
        