
# This is a comment. No /* */ or // needed — just #

# Python: 
#   no braces... indentation is key!!
#   no semicolons
#   no types ... but we'll require them in CS 2100

def greet(name, times=1):
    """Docstrings use triple quotes and often replace Javadoc comments."""
    message = f"Hello, {name}! Welcome to Python."
    for i in range(min(times, 5)):
        print(message)


greet("Storm", 3)

def describe_conditions(temp_f, wind_mph=0, is_raining=False):
    """Returns a short weather report string given current conditions."""
    feels_like = temp_f

    if wind_mph > 10:
        feels_like -= 5          # wind makes it feel colder

    condition = "rainy" if is_raining else "clear"  # 
    alert = "Bring an umbrella!" if is_raining and temp_f < 60 else ""

    return f"{temp_f}°F, feels like {feels_like}°F, conditions: {condition}. {alert}".strip()


# No 'public static void main' — this file IS the program.
# Code at the top level just runs, top to bottom.

current_temp = 68
current_wind = 15
raining_now = True

report = describe_conditions(current_temp, wind_mph=current_wind, is_raining=raining_now)
print(report)

if current_wind > 20:
    print("High wind advisory in effect.")

# positional arguments vs keyword arguments
# also... if parameter has a default, then, argument is optional
report = describe_conditions(current_temp, current_wind)
print(report)


# No types, so what happens when an a value of a different type then 
# expected is sent to a function? 
# Try it!
