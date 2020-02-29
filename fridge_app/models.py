from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.question_text


class FoodModel(models.Model):
    user = models.CharField(max_length=15) # maybe autofill user to user.user_name but idk how?
    food_in = models.CharField(max_length=20)
    expiration_date = models.DateTimeField('expiration date')
    def __str__(self):
        return self.food_in