# Generated by Django 2.1.4 on 2019-09-08 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msc', '0008_auto_20190908_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutritiontips',
            name='pub_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
