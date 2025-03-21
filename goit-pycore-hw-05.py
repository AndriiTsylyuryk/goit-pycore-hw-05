# def caching_fibonacci():
#     cache = {}

#     def fibonacci(n):
#         if n <= 0: return 0 
#         if n == 1: return 1
#         if n in cache: return cache[n]

#         cache[n] = fibonacci(n-1) + fibonacci(n-2)
#         return cache[n]
#     return fibonacci

# fibonacci_func = caching_fibonacci()
# print(fibonacci_func(15))

# ////////////////////////////////////////////////////////////
# import re
# from typing import Callable

# def generator_numbers(str): 
#     pattern = r'(?<!\S)[+-]?\d+(?:\.\d+)?(?!\S)'
#     nums_from_str = re.findall(pattern, str)

#     for i in nums_from_str:
#         yield float(i)


# def sum_profit(text: str, func: Callable):
#     gen = func(text)
#     sum = 0
#     for i in gen:
#         sum += i
#     return sum 


# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}")

# ////////////////////////////////////////////////////////////

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if isinstance(e, KeyError):
                return "This contact does not exist."
            elif isinstance(e, ValueError):
                return "Give me name and phone, please."
            elif isinstance(e, IndexError):
                return "Not enough arguments provided."
            else:
                return f"Something went wrong: {e}"
    return inner
        
@input_error
def add_contact(args, contacts):
    if len(args) < 2: 
        return 'Not enough info'
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_phone(args, contacts):
    if len(args) < 2: 
        return 'Not enough info'
    name, phone = args
    if name in contacts:
        contacts[name] = phone
    return 'Contact phone number was changed'

@input_error
def show_user_phone(args, contacts):
    if not args:  
        return "No name provided."
    name = args[0]  
    if name in contacts:
        return contacts[name]
    return "Contact not found."

        
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(contacts)
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == 'phone':
            print(show_user_phone(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()