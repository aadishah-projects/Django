from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        # print(recipe_name)
        # print(recipe_description)
        # print(recipe_image)
        Recipe.objects.create( 
            recipe_name =recipe_name  ,
            recipe_description = recipe_description  ,
            recipe_image = recipe_image
        )
        return redirect('/recipes/')
    
    queryset = Recipe.objects.all()

    if request.GET.get('search'): #automatically gets the data from front to back without method post
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search')) 


    context = {"page":"Recipes",
               'recipes': queryset }
    return render(request, 'recipes2.html',context)


def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    print("!DATA DELETED")
    return redirect('/recipes/')

def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/recipes/')
    
    context = {'recipe': queryset}
    return render(request, 'update_recipes.html', context)

def login_page (request):
    return render(request, "login.html")


def register_page (request):

    if request.method == "POST":
        data = request.POST
        # user_name = data.get('user_name')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        emailaddress = data.get('emailaddress')
        password = data.get('password')
        
        user = User.objects.filter(username = emailaddress)

        if user.exists():
            print("""______________________________ 
Registration Failed
--------------------------------""")
            return redirect('/register/')
            
        user  = User.objects.create( 
            first_name =first_name  ,
            last_name = last_name,
            username = emailaddress 
        )
        user.set_password(password) #for encryption
        user.save()

        return redirect('/register/')


    return render(request, "register.html")
