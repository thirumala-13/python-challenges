def greet(name):
    """
    TODO:
    Return a greeting message for the given name.

    The message format must be exactly: "Hello, {name}!"

    Example:
        greet("Alice") should return "Hello, Alice!"
        greet("Bob")   should return "Hello, Bob!"

    Hint: Use an f-string like this: f"Hello, {name}!"
    """
    
    return f"Hello, {name}!"


def describe_yourself(name, role):
    """
    TODO:
    Return a sentence introducing a person by their name and role.

    The message format must be exactly: "My name is {name} and I am a {role}."

    Example:
        describe_yourself("Maria", "software engineer")
        should return "My name is Maria and I am a software engineer."

    Note: There is a period (.) at the end of the sentence.
    """
    
    return f"My name is {name} and I am a {role}."
    


def format_greeting(greeting, name):
    """
    TODO:
    Combine a greeting word with a name and return the resulkuyut.

    The message format must be exactly: "{greeting}, {name}!"

    Example:
        format_greeting("Good morning", "Carlos")
        should return "Good morning, Carlos!"

        format_greeting("Hi", "World")
        should return "Hi, World!"

    Note: There is a comma and space between the greeting and the name.
    """
    return f"{greeting}, {name}!"