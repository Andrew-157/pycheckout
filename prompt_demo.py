from prompt_toolkit.shortcuts import choice

try:
    result = choice(
        message="Please choose a branch:",
        options=[
            ("pizza", "Pizza"),
            ("salad", "Salad"),
        ]
    )
except KeyboardInterrupt:
    print("fhjhfhfhfhf")

print(f"You chose: {result}")
