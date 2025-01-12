from django.shortcuts import render, get_object_or_404
from .models import Dish, UserDish
from .forms import addDishForm, addMealsForm
from django.contrib import messages 

# Create your views here.
def dishes_list(request):
    if request.method == 'POST':
        form = addMealsForm(request.POST)
        if form.is_valid():
            newUserDish = UserDish(user=request.user,
                                   dish=Dish.objects.get(id=form.cleaned_data['dish']),
                                   time_of_consumption=form.cleaned_data['time_of_consumption'],
                                   number_of_servings=form.cleaned_data['number_of_servings'])
            newUserDish.save()
        else:
            messages.error(request, "Error")
            raise Exception("Error")
    form = addMealsForm()
    dishes = Dish.objects.all().filter(is_published=Dish.Status.PUBLISHED)
    return render(request,
                  'dishes/list.html',
                  {'dishes': dishes,
                   "form": form})


def dish_detail(request, id):
    dish = get_object_or_404(Dish,
                             id=id)
    return render(request,
                  'dishes/detail.html',
                  {'dish': dish})


def add_dish(request):
    form = addDishForm()
    return render(request,
                  'dishes/add_dish.html',
                  {'form': form,
                   'request': request})