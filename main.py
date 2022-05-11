recipes = [
    {"name": "whiskey sour", "ingredients" : ["whiskey", "sugar", "lemon juice", "sugar", "egg whites", "angostura"]},
]

# type(recipes)



#first, what I want is for my program to search the list Recipes and return True if it finds the name of the recipe inputed (inputted? inputtted?) - UserInput. by this I just want to test a basic search function that I'll prob have to create

user_recipe = input("Enter a recipe. We'll see if we know it!")

#FOR each value related to "name" inside Recipes,
#  COMPARE value to UserInput - use find?
#   IF UserInput == Value
#       PRINT "recipe found"
#   ELSE
#       PRINT "recipe not found"
# 
# found this online, might be helpful
def search(recipes, user_recipe):
    for i in range(len(recipes)):
        if list[i] == user_recipe:
            return True
    return False


#this is not working lol
user_liquor = input("What liquor or ingredient do you have today?")

if "whiskey" in recipes:
    print("recipe found!")
else:
    print("No recipe found. Try something else")


