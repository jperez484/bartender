import random

questions = {
    "strong": "Ye like yer drinks strong eh?",
    "salty": "Ye like it with a salty tangy wangy?",
    "bitter": "Are ye a lubber who likes it bitter with a no spitter?",
    "sweet": "Would ye like a bit of sweet poison to tickle yer fancy?",
    "fruity": "Are ye one for a fruity tooty finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity": ["slice of melon", "dash of passion fruit", "crushed blueberries"],
}


def questions_func():

    questions_dictionary_new = {}

    for thing in questions: 
        #print(questions[thing])
        x =input(questions[thing])
        if x in {"Yes","Y", "yes", "y"}:
            #dictionary (assign boolean value)
            #see sample above
            #x_choice = random.choice(ingredients[thing])
            #ingredients_choices.append(x_choice)
            questions_dictionary_new[thing] = True
        else:
            questions_dictionary_new[thing] = False
            
    return questions_dictionary_new 

def drink_func(questions_dictionary_new):
    
    ingredients_choices = []
    for type in questions_dictionary_new:
        if  questions_dictionary_new[type] == True:
            x_choice = random.choice(ingredients[type])
            ingredients_choices.append(x_choice)
    
    return ingredients_choices

def main():
    
    drink_fun ={
    "adj": ["Funny", "Hot", "Electic", "Wet", "Blazing", "Curly"],
    "noun": ["Flamingo", "WildFlower", "Panther", "Bison", "Bulldog"],
    
    }

    drink_name = random.choice(drink_fun["adj"])+" "+random.choice(drink_fun["noun"])
    
    preferences = questions_func() 
    drink_ingredients = drink_func(preferences)  
    
    if drink_ingredients ==[]:
        print("")
        print("")
        print("There's no drink here for Picky scallywags!")
    else:
        print("")
        print("")
        print("Your drink is called the {}".format(drink_name))
        print("Made up of a {}".format(", ".join(drink_ingredients)))
    
if __name__ == '__main__':
    main()
    
    #for next week
    #drink func filled out so it actually works
    #drink_name not be global as is