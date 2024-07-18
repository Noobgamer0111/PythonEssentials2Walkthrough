def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n


print(reciprocal(2))
print(reciprocal(0))
    
# Output:
# Everything went fine
# It's time to say goodbye
# 0.5
# Division failed
# It's time to say goodbye
# None