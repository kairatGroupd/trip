# Generated by Django 3.2.4 on 2021-07-03 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_lodging_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lodging',
            name='category',
            field=models.CharField(choices=[('h', 'Hotel'), ('y', 'Yurts'), ('a', 'Apartments'), ('o', 'Other')], max_length=1, null=True),
        ),
    ]
