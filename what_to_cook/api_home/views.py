from django.shortcuts import render
from .forms import IngredientsForm
from . import functions
from . import models
from .models import ingredients_list
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


# from dotenv import load_dotenv          >>> A FINIR D'IMPLEMENTER (fichier .env dans bon repertoire)


def login(request):
    return render(request,'pages_main/login.html')

def page_home(request):
    return render(request,'pages_main/home.html')


@login_required
def create_recipe(request):
    form = IngredientsForm(request.POST)
    ingredient_choices = ingredients_list
    if request.method == "POST":
        if form.is_valid():
            form.save()
            print(functions.findrecipe(functions.ingredients_from_UI)["RecipeName"])
            print(dict(form.cleaned_data))
        return render(request, 'pages_main/cedric.html', {'form': form })
    else:
        return render(request, 'pages_main/cedric.html', {'form': form, 'ingredient_choices': ingredient_choices })





class SignupPage(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


