# Generated by Django 5.0.3 on 2024-04-11 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_itemreview_itemreviewlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnSaleLits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('savePercentage', models.PositiveIntegerField()),
                ('saleEndTime', models.DateTimeField()),
                ('itemData', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sellitemlist')),
            ],
        ),
    ]