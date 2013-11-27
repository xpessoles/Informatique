def division(a,b):
    reste = a
    quotient = 0
    while reste > b:
        reste = reste -b
        quotient = quotient + 1
    print("reste ", reste)
    print("quotient ", quotient)

division(6,10)
