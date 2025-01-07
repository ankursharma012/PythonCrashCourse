responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name: ")
    age = input("\n What is your age: ")
    responses[name] = age

    prompt = input("Enter 'quit' to stop. ")
    if prompt == 'quit':
        polling_active = False

for name, age in responses.items():
    print(f"\n{name} is {age} years old.")