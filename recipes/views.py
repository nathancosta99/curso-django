from django.shortcuts import render, get_list_or_404, get_object_or_404
from recipes.models import Recipe


def home(request):
    recipes = get_list_or_404(Recipe.objects.filter(
        is_published=True
        ).order_by('-id'))

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name}  - Category | '
    })


def category(request, category_id):

    recipes = get_list_or_404(Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id'))  # noqa: E501

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name}  - Category | '
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
