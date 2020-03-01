from django.db import models



class Food(models.Model):
    user = models.CharField(max_length=15) # maybe autofill user to user.user_name but idk how?
    food_name = models.CharField(max_length=100)
    exp_date = models.DateTimeField('expiration date')
    def __str__(self):
        return self.food_in
