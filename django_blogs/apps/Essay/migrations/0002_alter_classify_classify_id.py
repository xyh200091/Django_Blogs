# Generated by Django 4.0.4 on 2022-06-10 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Essay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classify',
            name='Classify_Id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
    ]
