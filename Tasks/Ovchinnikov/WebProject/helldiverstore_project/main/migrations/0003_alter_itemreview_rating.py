# Generated by Django 5.0.3 on 2024-04-07 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_itemreview_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemreview',
            name='rating',
            field=models.PositiveIntegerField(),
        ),
    ]
