# Generated by Django 4.0.5 on 2023-04-03 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0017_question_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='publish',
        ),
        migrations.AddField(
            model_name='comment',
            name='publish',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
