

###########################################
# While default parameter values are useful, beward that if the default
# value is an object, aliases for it can be used which can have unintended side effects.
# This is demonstrated in the example below... READ THE WARNING from Pylint!
# Use Python Tutor to visualize the code at lines 9-18.

def send_message_and_cc_self(message: str, sender: str, recipients: list[str] = []) -> None:
    '''Demo for distributing a message to several recipients and CC sender'''
    recipients.append(sender) # add sender to recipients so they get a copy as well
    for r in recipients: # send message to each recipient
        print(f"Sending '{message}' from {sender} to {r}")

send_message_and_cc_self("note to self", "Rasika") # self-only message
send_message_and_cc_self("use RSA next time", "Eve", ["Alice", "Bob"]) # message to multiple people
send_message_and_cc_self("super secret", "admin") # another self-only message

print('\n' * 2, '-' * 60, '\n' * 2)
###########################################
# Demo of a function that accepts variable arguments
# The type of the parameter is a tuple, consisting of
# all the arguments sent by the caller. 
# A tuple is an immutable sequence of items and can be used similar
# to one would use a list, with the exception that list has mutator methods
# and tuple doesn't... it can't since it's immutable.

def count_letters(*args: str) -> int:
    """Returns the number of letters (a-z, A-Z) in the string inputs"""
    print(f"Parameter: {args}, data type: {type(args)}")   # it's a tuple!
    count : int = 0
    for value in args:
        for c in value.lower():
            if c.isalpha():
                count += 1

    return count

total : int = count_letters('3 arguments', 'World Of Variable', '31 letters')
print(f'1st example: there are {total} letters')

total = count_letters('5 arguments', 'one2', '3', 'four', '9 + 3 + 4 = 16')
print(f'2nd example; there are {total} letters')

print('\n' * 2, '-' * 60, '\n' * 2)
###########################################
# Python print() function takes any number of arguments
# We can write our own functions that take variable number of arguments.

print()
print('hello')
print('hello', 42 / 4, 'variable', 2 ** 3, 'argument', 'list')

# Note use of type object, that will accept any type
# This is different from example in the notes which can only print strings
#
def print_args(*args: object) -> None:
    """Print each argument on a separate line"""
    for item in args:
        print(item)

print_args(1, "allows any type", 3.2)

print('\n' * 2, '-' * 60, '\n' * 2)
###########################################
# Keyword arguments work similarly, though the parameter type is a dictionary
# as we need to retain the keyword name and its value.
def print_kwargs(**kwargs: object) -> None:
    """Print each argument on a separate line"""
    print(f"Parameter type: {type(kwargs)}")
    for argument_name, argument_value in kwargs.items():
        print(f'{argument_name}: {argument_value}')

print_kwargs(item = 'any', debug = True, category = 'log', count = 5)
