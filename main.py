# sys.path.append(".")

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

while user_input != "no": 
    for i in range(len(Menu.RECIPES)):
        if Menu.RECIPES[i]["name"] == user_input or user_input in  Menu.RECIPES[i]["ingredients"]:
            print(Menu.RECIPES[i]["name"])
    user_input = input("You got any more liquor in your bar? Want to check another recipe?").lower()
    if user_input == "no":
        break

print("Thank you for drinking with Cocktail Fix today. Cheers!")
  


#first, what I want is for my program to search the list Menu.RECIPES and return True if it finds the name of the recipe inputed (inputted? inputtted?) - UserInput. by this I just want to test a basic search function that I'll prob have to create

# user_recipe = input("Enter a recipe. We'll see if we know it!")

# #FOR each value related to "name" inside Recipes,
# #  COMPARE value to UserInput - use find?
# #   IF UserInput == Value
# #       PRINT "recipe found"
# #   ELSE
# #       PRINT "recipe not found"
# # 
# # found this online, might be helpful
# def search(recipes, user_recipe):
#     for i in range(len(recipes)):
#         if list[i] == user_recipe:
#             return True
#     return False


# #this is not working lol
# user_liquor = input("What liquor or ingredient do you have today?")

# if "whiskey" in recipes:
#     print("recipe found!")
# else:
#     print("No recipe found. Try something else")


