# Generated by Django 3.0 on 2019-12-17 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_auto_20191217_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datacolumn',
            name='column_max_length',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
