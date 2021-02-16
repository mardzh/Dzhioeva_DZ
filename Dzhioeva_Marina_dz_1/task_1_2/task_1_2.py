if __name__ == '__main__':
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