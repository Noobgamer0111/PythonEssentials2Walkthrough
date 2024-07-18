try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())
    
# Output:
# invalid literal for int() with base 10: 'Hello!'
# invalid literal for int() with base 10: 'Hello!'