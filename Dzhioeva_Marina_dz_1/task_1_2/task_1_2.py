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

cube = 0
for i in range (1, 1000):
    if(i %2 != 0):
        cube = i **3
        dex = 1
        count = 0
        while(1):
            if(cube > dex):
                count += 1
                dex *= 10
            else:
                dex //= 10
                break

        sum = 0
        while(count != 0):
            count -= 1
            a = cube // dex
            sum += a
            cube -= dex * a
            dex //= 10

        if(sum % 7 == 0):
            print("число: ", i)
            print("sum: ", sum)




