# Generated by Django 3.0 on 2019-12-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_auto_20191217_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='template_name',
            field=models.CharField(blank=True, help_text='Example: “flatpages/contact_page.html”. If this isn’t provided, the system will use “flatpages/default.html”.', max_length=70, verbose_name='template name'),
        ),
    ]
