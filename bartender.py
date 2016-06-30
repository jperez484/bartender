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

drink_fun ={
    "adj": ["Funny", "Hot", "Electic", "Wet", "Blazing", "Curly"],
    "noun": ["Flamingo", "WildFlower", "Panther", "Bison", "Bulldog"],
    
}

drink_name = random.choice(drink_fun["adj"])+" "+random.choice(drink_fun["noun"])

ingredients_choices = []

for thing in questions: 
    #print(questions[thing])
    x =input(questions[thing])
    if x in {"Yes","Y", "yes", "y"}:
        x_choice = random.choice(ingredients[thing])
        ingredients_choices.append(x_choice)

if ingredients_choices ==[]:
    print("There's no drink here for Picky scallywags!")
else:
    print("your drink is called the {}".format(drink_name))
    print("Made up of a: {}".format(", ".join(ingredients_choices)))