from view import View
from menu import Menu
view = View()
print(view)

#Greet the user: "Welcome to Cocktail Fix!"
#Ask user: "What liquor or ingredient do you have in your bar today?"
#get user input
#compare to recipes. if not found, print "Sorry, you're out of luck." Skip to line 21.
#   If found, app will return the name(s) of recipe(s) containing that ingredient: "Jackpot! You could make those drinks: (...)"
#Ask user: "Which recipe would you like to learn today?"
#get user input (number)
#display detailed recipe 
#Ask user: "would you like to see the results again? Y/N". If Yes, repeat. If no, go to end.
#Ask user: "You got any more liquor in your bar? Want to check another recipe?"
#get user input
#if Y, back to top
#if N, go to end
#End: "Thank you for drinking with Cocktail Fix today. Cheers!"

print("Welcome to Cocktail Fix!")

user_input = input("What liquor or ingredient do you have in your bar today?").lower()
results = []

for i in range(len(Menu.RECIPES)):
    if Menu.RECIPES[i]["name"] == user_input or user_input in  Menu.RECIPES[i]["ingredients"]:
        # print(i, Menu.RECIPES[i]["name"])
        results.append(Menu.RECIPES[i]["name"])

print("These are the cocktails we've found for you.")        
print(results)

user_input = input("Which recipe would you like to learn today? Choose a recipe.").lower()
print(user_input)
for i in range(len(Menu.RECIPES)):
    if Menu.RECIPES[i]["name"] == user_input:
        for ingredient in Menu.RECIPES[i]["ingredients"]:
            print("- ", ingredient)
        # print(Menu.RECIPES[i]["ingredients"])
    

print("Thank you for drinking with Cocktail Fix today. Cheers!")
  




