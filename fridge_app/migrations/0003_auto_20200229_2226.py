# Generated by Django 3.0.3 on 2020-02-29 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridge_app', '0002_foodmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=15)),
                ('food_name', models.CharField(max_length=100)),
                ('exp_date', models.DateTimeField(verbose_name='expiration date')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='FoodModel',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]