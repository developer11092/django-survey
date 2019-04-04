# Generated by Django 2.1.1 on 2019-04-03 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='image',
        ),
        migrations.AddField(
            model_name='question',
            name='images',
            field=models.FileField(blank=True, help_text='Upload either image or any other field', null=True, upload_to='survey/images/questions/%Y/%m/%d/', verbose_name='File Upload'),
        ),
    ]
