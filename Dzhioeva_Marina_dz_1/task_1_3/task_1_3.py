# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
while(1):
    i = int(input("Введите число: "))

    if(i >=2 and i <=4):
        print( i, 'процента')
    elif (i == 1):
        print(i, 'процент')
    elif(5<= i <= 10):
        print(i, 'процентов')