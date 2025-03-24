def factorial():
    num = int(input("Enter a number: "))
    if num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for i in range(1, num+1):
          fact *= i
        print(fact)
factorial()


