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
dr = random.choice(drink_fun["adj"])
na = random.choice(drink_fun["noun"])

drink_name = dr+" "+na
a_choice =''
b_choice =''
c_choice =''
d_choice =''
e_choice =''


a = input(questions["strong"])

if a in {"Yes","Y", "yes", "y"}:
    #print(ingredients["strong"])
    a_choice = random.choice(ingredients["strong"])
    #print(random.choice(ingredients["strong"]))
    #print(a_choice)
else:
    a_choice ="No"
    
b = input(questions["salty"])

if b in {"Yes","Y", "yes", "y"}:
    #print(ingredients["salty"])
    b_choice = random.choice(ingredients["salty"])
    #print(random.choice(ingredients["salty"]))
    #print(b_choice)
else:
    b_choice ="No"
    
c = input(questions["bitter"])

if c in {"Yes","Y", "yes", "y"}:
    #print(ingredients["bitter"])
    c_choice = random.choice(ingredients["bitter"])
    #print(random.choice(ingredients["bitter"]))
    #print(c_choice)
else:
    c_choice ="No"
    
d = input(questions["sweet"])

if d in {"Yes","Y", "yes", "y"}:
    #print(ingredients["sweet"])
    d_choice = random.choice(ingredients["sweet"])
    #print(random.choice(ingredients["sweet"]))
    #print(d_choice)
else:
    d_choice ="No"
    

e = input(questions["fruity"])

if e in {"Yes","Y", "yes", "y"}:
    #print(ingredients["fruity"])
    e_choice = random.choice(ingredients["fruity"])
    #print(random.choice(ingredients["fruity"]))
    #print(e_choice)
else:
    e_choice ="No"
    
if a_choice == 'No':
    if b_choice == 'No':
        if c_choice == 'No':
            if d_choice =='No':
                if e_choice =='No':
                    print("There's no drink here for Picky scallywags!")
else:
                    print("your drink is called the {}".format(drink_name))
                    print("Made up of a: {}, {}, {}, {}, {}".format(a_choice,b_choice,c_choice,d_choice,e_choice))