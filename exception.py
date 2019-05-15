try:
    x = input("give the input")
    x = int(x)
    print(x)
    print("print after error")

except:
    print("Error occured")

finally:
    print("It always executes")

print("End of file")
