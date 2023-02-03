# Generated by Django 4.1.5 on 2023-01-25 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habit_tracker", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="modelhabit", name="break_streak",),
        migrations.AddField(
            model_name="modelhabit",
            name="worst_streak",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="modelhabit",
            name="current_streak",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="modelhabit",
            name="max_streak",
            field=models.IntegerField(default=0),
        ),
    ]
