res = lambda num: num * num
# lambda - keyword
# num - parameter


def outside_function():
    def inside_function():
        print("inside function")
    inside_function()

outside_function()
# anotherFunction
