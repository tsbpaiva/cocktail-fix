from menu import Menu

# Greet the user: "Welcome to Cocktail Fix!"
# Ask user: "What liquor or ingredient do you have in your bar today?"
# get user input
# compare to recipes. if not found, print "Sorry, you're out of luck." Skip to line 13.
#   If found, app will return the name(s) of recipe(s) containing that ingredient: "Jackpot! You could make those drinks: (...)"
# Ask user: "Which recipe would you like to learn today?"
# get user input (number) 
# display detailed recipe 
# Ask user: "You got any more liquor in your bar? Want to check another recipe?"
# get user input
# if Y, back to top
# if N, go to end
# End: "Thank you for drinking with Cocktail Fix today. Cheers!"

# welcome user
print("Welcome to Cocktail Fix! 🍸🍸🍸")
user_input = ""

while user_input != "no":

    # getting user input (i.e., the liquor they want to try)
    user_input = input("What liquor or ingredient do you have in your bar today? 🧐 ").lower()
    results = []

    # findind recipes; populating results list
    for i in range(len(Menu.RECIPES)):
        if Menu.RECIPES[i]["name"] == user_input or user_input in Menu.RECIPES[i]["ingredients"]:
            results.append(Menu.RECIPES[i])
    
    # displaying recipe options
    if bool(results):
        print("You're in luck 🍀 ! With", user_input, "you can make these cocktails:")        
        for i in range(len(results)):
            print(i + 1, "-", results[i]["name"].title())
        
        user_index = input("Which cocktail would you like to learn today? Choose a number.").lower()
        user_index = int(user_index) - 1
    
        print("Just make yourself a nice", results[user_index]["name"], "and relax 🍹 ! Here's the recipe 📝 :")
        for ingredient in results[user_index]["ingredients"]:
            print("- ", ingredient.capitalize())
        user_input = input("You got any more liquor in your bar 👀 ? Want to check another recipe? Just type yes or no.")

    else:
        print("You're out of luck today, pal. We don't have any cocktails that use", user_input+" 😞 ... But don't fret! Let's try that again! 🙌🙌🙌")
        user_input = input("You got any more liquor in your bar 👀 ? Want to check another recipe? Just type yes or no.")

# goodbyes    
print("Thank you for drinking with Cocktail Fix today. Cheers!")
print("🥂")
print("🥂")


