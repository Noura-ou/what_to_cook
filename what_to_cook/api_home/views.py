from django.shortcuts import render
from .forms import IngredientsForm
from . import functions
from .models import ingredients_list

# from dotenv import load_dotenv          
# A FINIR D'IMPLEMENTER (fichier .env dans bon repertoire)
# load_dotenv()

def login(request):
    return render(request,'pages_main/login.html')

def page_home(request):
    return render(request,'pages_main/home.html')

def create_recipe(request):
    form = IngredientsForm(request.POST)
    ingredient_choices = ingredients_list
    ingredients_from_UI =[]
    if request.method == "POST":
        if form.is_valid():
            print(form.data)
            form.save()
            # print(functions.findrecipe(functions.ingredients_from_UI)["RecipeName"])
            print(str("form.cleaned_data").upper(),form.cleaned_data)
            for key,values in form.cleaned_data.items():
                # cat2 = list(ingredient_choices.keys())[0]
                # print("cat2=",cat2)
                print("ing choices=",ingredient_choices)
                cpt = 0
                print(ingredient_choices)
                for value in values:
                    if value == key:
                        ingredients_from_UI.append(ingredient_choices[key][cpt].lower())
                        cpt += 1

            print(ingredients_from_UI)
            print(functions.findrecipe(ingredients_from_UI)["RecipeName"])
        return render(request, 'pages_main/cedric.html', {'form': form })
    else:
        return render(request, 'pages_main/cedric.html', {'form': form, 'ingredient_choices': ingredient_choices })

