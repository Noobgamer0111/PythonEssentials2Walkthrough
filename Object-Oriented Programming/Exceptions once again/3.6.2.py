def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)
    
# Output:
# # BaseException
# #   +---Exception
# #   |   +---TypeError
#    |   +---StopAsyncIteration
#    |   +---StopIteration
#    |   +---ImportError
#    |   |   +---ModuleNotFoundError
#    |   |   +---ZipImportError
#    |   +---OSError
#    |   |   +---ConnectionError
#    |   |   |   +---BrokenPipeError
#    |   |   |   +---ConnectionAbortedError
#    |   |   |   +---ConnectionRefusedError
#    |   |   |   +---ConnectionResetError
#    |   |   +---BlockingIOError
#    |   |   +---ChildProcessError
#    |   |   +---FileExistsError
#    |   |   +---FileNotFoundError
#    |   |   +---IsADirectoryError
#    |   |   +---NotADirectoryError
#    |   |   +---InterruptedError
#    |   |   +---PermissionError
#    |   |   +---ProcessLookupError
#    |   |   +---TimeoutError
#    |   |   +---UnsupportedOperation
#    |   |   +---ItimerError
#    |   +---EOFError
#    |   +---RuntimeError
#    |   |   +---RecursionError
#    |   |   +---NotImplementedError
#    |   |   +---_DeadlockError
#    |   +---NameError
#    |   |   +---UnboundLocalError
#    |   +---AttributeError
#    |   +---SyntaxError
#    |   |   +---IndentationError
#    |   |   |   +---TabError
#    |   +---LookupError
#    |   |   +---IndexError
#    |   |   +---KeyError
#    |   |   +---CodecRegistryError
#    |   +---ValueError
#    |   |   +---UnicodeError
#    |   |   |   +---UnicodeEncodeError
#    |   |   |   +---UnicodeDecodeError
#    |   |   |   +---UnicodeTranslateError
#    |   |   +---UnsupportedOperation
# ...
# ...
#    |   +---AssertionError
#    |   +---ArithmeticError
#    |   |   +---FloatingPointError
#    |   |   +---OverflowError
#    |   |   +---ZeroDivisionError
#    |   +---SystemError
#    |   |   +---CodecRegistryError
#    |   +---ReferenceError
#    |   +---MemoryError
#    |   +---BufferError
#    |   +---Warning
#    |   |   +---UserWarning
#    |   |   +---DeprecationWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---SyntaxWarning
#    |   |   +---RuntimeWarning
#    |   |   +---FutureWarning
#    |   |   +---ImportWarning
#    |   |   +---UnicodeWarning
#    |   |   +---BytesWarning
#    |   |   +---ResourceWarning
#    |   +---Error
#    +---GeneratorExit
#    +---SystemExit
#    +---KeyboardInterrupt