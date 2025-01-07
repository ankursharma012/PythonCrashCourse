pizza = {
    'crust':'thick',
    'toppings':['mushroom', 'chicken']
}

print(f"You ordered a {pizza['crust']}-crust pizza"
      "with the toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
