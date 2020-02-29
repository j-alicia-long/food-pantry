from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from fridge_app.forms import FoodForm
# from django.views.generic.edit import FormView

# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def about(request):
    return render(request, 'about.html')

# @login_required
# def FoodView(formView):
#     template name = 'food_form.html'
#     form_class = FoodForm
#     success_url = '/index/'

#     def form_valid(self, form):
#         return super().form_valid(form)