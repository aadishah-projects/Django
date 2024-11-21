from django.shortcuts import render

# Create your views here.

def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        print(recipe_name)
        print(recipe_description)
        print(recipe_image)
    
    context = {"page":"recipes"}
    return render(request, 'recipes.html',context)