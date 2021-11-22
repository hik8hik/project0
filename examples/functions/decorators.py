# HACK :  FUNCTIONAL PROGRAMMMING PARADIME
def announce(f):
    def wrapper():
        print("About to run a function...")
        f()
        print("Done running the function")
    return wrapper


@announce # ADDED HERE TO WRAP THIS FUNCTION IN BETWEEN PRINT && PRINT
#(as function f())
def hello():
    print("Hello World!")


hello()
