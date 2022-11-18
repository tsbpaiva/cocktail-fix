from menu import RECIPES

class Main:
    def find_cocktails(self, user_input):
        search_results = []
        for recipe in range(len(RECIPES)):
            if RECIPES[recipe]["name"] == user_input or user_input in RECIPES[recipe]["ingredients"]:
                search_results.append(RECIPES[recipe])
        results = {"user input": "vodka", "search results": search_results}
        return results

    def display_options(self, search_results):
        print('inside display_options')
        for i in range(len(search_results)):
            print(i + 1, "-", search_results[i]["name"].title())
        # return search_results

    # HERE IS THE PROBLEM! 
    def display_recipe(self, result_recipe):
        print('inside display recipe')
        print("Just make yourself a nice", result_recipe['name'], "and relax 🍹 ! Here's the recipe 📝 :")
        for ingredient in result_recipe["ingredients"]:
            print("- ", ingredient.capitalize())

    def run(self):
        user_input = ""
        while user_input != "no":
            # getting user input (i.e., the liquor they want to try)
            user_input = input("What liquor or ingredient do you have in your bar today? 🧐 ").lower()
            # findind recipes; populating RESULTS list
            results = self.find_cocktails(user_input)
            # displaying cocktail options
            if bool(results['search results']):
                print("You're in luck 🍀 ! With", results['user input'], "you can make these cocktails:")        
                self.display_options(results['search results'])
                user_index = int(input("Which cocktail would you like to learn today? Choose a number.")) - 1
                result_recipe = results['search results'][user_index]
                #displaying recipe:
                self.display_recipe(result_recipe)
            else:
                print("You're out of luck today, pal. We don't have any cocktails that use", user_input+" 😞 ... But don't fret! Let's try that again! 🙌🙌🙌")
            user_input = input("You got any more liquor in your bar 👀 ? Want to check another recipe? Just type yes or no.")

# to test using this very file:
# if __name__ == '__main__':
#     Main().run()