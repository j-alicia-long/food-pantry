from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic

from .models import Food
# from fridge_app.forms import FoodForm

@login_required
def index(request):
    return render(request, 'fridge_app/index.html')

def about(request):
    return render(request, 'fridge_app/about.html')

# Can't use @login_required decorator on a class
@method_decorator(login_required, name='dispatch')
class LogFoodView(generic.CreateView):
    model = Food
    template_name = 'food_form.html'
    success_url = 'index/'
    fields = ['user', 'food_name', 'exp_date']

# May want to use a form class instead for more customization
# @login_required
# def FoodView(request):
#     template_name = 'food_form.html'
#     form_class = FoodForm
#     success_url = 'index/'
    # def form_valid(self, form):
    #     return super().form_valid(form)
