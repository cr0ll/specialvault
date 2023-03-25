import random

print("A small program brought to you by cr0ll :)")

i = 4
while i < 5:

    start = int(input("Enter start value: "))
    end = int(input("Enter end value: "))

    if start < end:

        number = random.randint(start, end)
        numberQuanity = (end - start)
        numberChange = (100 / numberQuanity)

        print("Random amount from", start, "to", end, "is:", number, ("."))
        print("It is", numberChange, "change of this number.")
        print("-----------------------------------------------")

    else:
        print("Start value cannot be bigger, than end value!")
        print("-----------------------------------------------")



