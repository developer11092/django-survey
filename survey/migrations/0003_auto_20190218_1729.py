# Generated by Django 2.1.1 on 2019-02-18 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20190218_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='vid_url',
            field=models.CharField(blank=True, default='https://www.youtube.com/embed/', max_length=300, verbose_name='Url'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=300, verbose_name='Question'),
        ),
    ]
