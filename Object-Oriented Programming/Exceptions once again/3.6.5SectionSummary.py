# 1. The else: branch of the try statement is executed when there has been no exception during the execution of the try: block.

# 2. The finally: branch of the try statement is always executed.

# 3. The syntax except Exception_Name as an exception_object: lets you intercept an object carrying information about a pending exception. The object's property named args (a tuple) stores all arguments passed to the object's constructor.

# 4. The exception classes can be extended to enrich them with new capabilities, or to adopt their traits to newly defined exceptions.

try:
    assert __name__ == "__main__"
except:
    print("fail", end=' ')
else:
    print("success", end=' ')
finally:
    print("done")
 
# The code outputs: success done.