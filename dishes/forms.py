from django import forms
from .models import DishesType, UserDish


class addDishForm(forms.Form):
    name = forms.CharField(label='Название')
    dish_types = forms.ModelMultipleChoiceField(queryset=DishesType.objects.all(),
                                                required=False,
                                                widget=forms.CheckboxSelectMultiple,
                                                label='Типы блюда')


class addMealsForm(forms.Form):
    dish = forms.IntegerField(widget=forms.NumberInput(attrs={"readonly":True}), label="Блюдо")
    # user = forms.IntegerField(widget=forms.HiddenInput)
    time_of_consumption = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": 'form-control', "type":"datetime-local"}), label='Время употребления')
    number_of_servings = forms.IntegerField(widget=forms.NumberInput(attrs={"class": 'form-control'}), label='Количество порций', required=False, min_value=1)

