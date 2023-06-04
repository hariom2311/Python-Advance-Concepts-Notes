# Function Inside function and decorator

def addOne(myFunc):
    """
    Decorator function that adds 1 to the result of the decorated function.
    
    Args:
        myFunc: The function to be decorated.
        
    Returns:
        The decorated function that adds 1 to the result of myFunc.
    """
    def addOneInside(x):
        """
        Inner function that adds 1 to the result of myFunc.
        
        Args:
            x: The input argument for myFunc.
            
        Returns:
            The result of myFunc(x) plus 1.
        """
        print("adding One")
        return myFunc(x) + 1
    return addOneInside

def subThree(x):
    """
    Function that subtracts 3 from the input argument.
    
    Args:
        x: The input value.
        
    Returns:
        The result of subtracting 3 from x.
    """
    return x - 3

result = addOne(subThree)

print(subThree(5))  # Output: 2
print(result(5))  # Output: 3

# passing *args and **kwargs arguments
def addOne(myFunc):
    """
    Decorator function that adds 1 to the result of the decorated function,
    supporting arbitrary positional and keyword arguments.
    
    Args:
        myFunc: The function to be decorated.
        
    Returns:
        The decorated function that adds 1 to the result of myFunc.
    """
    def addOneInside(*args, **kwargs):
        """
        Inner function that adds 1 to the result of myFunc.
        
        Args:
            *args: Arbitrary positional arguments.
            **kwargs: Arbitrary keyword arguments.
            
        Returns:
            The result of myFunc(*args, **kwargs) plus 1.
        """
        print("adding One")
        return myFunc(*args, **kwargs) + 1
    return addOneInside

def subThree(x):
    """
    Function that subtracts 3 from the input argument.
    
    Args:
        x: The input value.
        
    Returns:
        The result of subtracting 3 from x.
    """
    return x - 3

result = addOne(subThree)

print(subThree(5))
print(result(5))

def addOne(myFunc):
    """
    Decorator function that adds 1 to the result of the decorated function,
    supporting arbitrary positional and keyword arguments.
    
    Args:
        myFunc: The function to be decorated.
        
    Returns:
        The decorated function that adds 1 to the result of myFunc.
    """
    def addOneInside(*args, **kwargs):
        """
        Inner function that adds 1 to the result of myFunc.
        
        Args:
            *args: Arbitrary positional arguments.
            **kwargs: Arbitrary keyword arguments.
            
        Returns:
            The result of myFunc(*args, **kwargs) plus 1.
        """
        print("adding One")
        return myFunc(*args, **kwargs) + 1
    return addOneInside

def subThree(x):
    """
    Function that subtracts 3 from the input argument.
    
    Args:
        x: The input value.
        
    Returns:
        The result of subtracting 3 from x.
    """
    return x - 3

subThree = addOne(subThree)

print(subThree(5))

# using decorator in this below code
def addOne(myFunc):
    """
    Decorator function that adds 1 to the result of the decorated function,
    supporting arbitrary positional and keyword arguments.
    
    Args:
        myFunc: The function to be decorated.
        
    Returns:
        The decorated function that adds 1 to the result of myFunc.
    """
    def addOneInside(*args, **kwargs):
        """
        Inner function that adds 1 to the result of myFunc.
        
        Args:
            *args: Arbitrary positional arguments.
            **kwargs: Arbitrary keyword arguments.
            
        Returns:
            The result of myFunc(*args, **kwargs) plus 1.
        """
        print("adding One")
        return myFunc(*args, **kwargs) + 1
    return addOneInside

@addOne
def subThree(x):
    """
    Function that subtracts 3 from the input argument.
    
    Args:
        x: The input value.
        
    Returns:
        The result of subtracting 3 from x.
    """
    return x - 3

print(subThree(5))

# another example of decorators
def smart_func(any_func):
    """
    Decorator function that swaps the input arguments if the first argument is smaller than the second argument.
    
    Args:
        any_func: The function to be decorated.
        
    Returns:
        The decorated function that swaps the input arguments if needed.
    """
    def inner(a, b):
        """
        Inner function that swaps the input arguments if necessary and calls any_func.
        
        Args:
            a: The first input argument.
            b: The second input argument.
            
        Returns:
            The result of calling any_func with the modified input arguments.
        """
        if a < b:
            a, b = b, a
        return any_func(a, b)
    return inner


def do_sub(a, b):
    """
    Function that subtracts b from a.
    
    Args:
        a: The first input value.
        b: The second input value.
        
    Returns:
        The result of subtracting b from a.
    """
    return a - b


call_func = smart_func(do_sub)
print(call_func(2, 4))

# write above code using decorator
def smart_func(any_func):
    """
    Decorator function that swaps the input arguments if the first argument is smaller than the second argument.
    
    Args:
        any_func: The function to be decorated.
        
    Returns:
        The decorated function that swaps the input arguments if needed.
    """
    def inner(a, b):
        """
        Inner function that swaps the input arguments if necessary and calls any_func.
        
        Args:
            a: The first input argument.
            b: The second input argument.
            
        Returns:
            The result of calling any_func with the modified input arguments.
        """
        if a < b:
            a, b = b, a
        return any_func(a, b)
    return inner

@smart_func
def do_sub(a, b):
    """
    Function that subtracts b from a.
    
    Args:
        a: The first input value.
        b: The second input value.
        
    Returns:
        The result of subtracting b from a.
    """
    return a - b

print(do_sub(4, 2))
