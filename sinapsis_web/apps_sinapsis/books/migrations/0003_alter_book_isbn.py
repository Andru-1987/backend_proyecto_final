# Generated by Django 4.2.2 on 2023-06-25 17:41

import apps_sinapsis.utils.validate_functions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(default='978-3-16-148410-0', max_length=17, validators=[apps_sinapsis.utils.validate_functions.validate_ISBN]),
        ),
    ]
