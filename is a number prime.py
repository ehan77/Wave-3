# INPUTS

numbe_r = int(input("Enter an integer: "))

if numbe_r > 1 :
    for i in range(2, numbe_r) :
        if (numbe_r % i) == 0 : 
            print(numbe_r , "is not a prime number.")
            break
    else :
        print(numbe_r , "is a prime number.")
else :
    print(numbe_r , "is not a prime number.")