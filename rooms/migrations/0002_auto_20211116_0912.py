# Generated by Django 3.2.9 on 2021-11-16 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='roomlocation',
            name='latitude',
            field=models.DecimalField(decimal_places=14, default=0.0, max_digits=16),
        ),
        migrations.AlterField(
            model_name='roomlocation',
            name='longitude',
            field=models.DecimalField(decimal_places=14, default=0.0, max_digits=17),
        ),
    ]
