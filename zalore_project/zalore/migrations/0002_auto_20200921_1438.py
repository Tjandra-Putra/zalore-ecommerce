# Generated by Django 3.1.1 on 2020-09-21 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zalore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
