# Generated by Django 3.2.4 on 2021-07-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsmodel',
            name='car_capacity',
            field=models.CharField(choices=[('S', '2-4'), ('M', '4-6'), ('L', '6-8')], max_length=1, null=True),
        ),
    ]
