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


#print(questions["strong"])

a = input(questions["strong"])

if a in {"Yes", "Y", "yes"}:
    #print(ingredients["strong"])
    print(random.choice(ingredients["strong"]))
    
a = input(questions["strong"])

if a in {"Yes", "Y", "yes"}:
    #print(ingredients["strong"])
    print(random.choice(ingredients["strong"]))
    
a = input(questions["strong"])

if a in {"Yes", "Y", "yes"}:
    #print(ingredients["strong"])
    print(random.choice(ingredients["strong"]))
    
a = input(questions["strong"])

if a in {"Yes", "Y", "yes"}:
    #print(ingredients["strong"])
    print(random.choice(ingredients["strong"]))
    


    

