# *args

def adder(*num):
    sum = 0
    for n in num:
        sum += n
    print("sum:", sum)


if __name__ == "__main__":
    adder(2)
    adder(2, 3, 4, 5)
    adder(10, 11, 2, 33, 444)