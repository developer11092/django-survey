# Generated by Django 2.1.1 on 2019-02-23 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0015_auto_20190223_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('text', 'Long text (multiple line)'), ('short-text', 'Short text (one line)'), ('radio', 'Radio Select'), ('select', 'Empty'), ('select-multiple', 'Select Multiple'), ('integer', 'Numeric'), ('select_image', 'Select Image'), ('add_date', 'Add Date'), ('add_image', 'Add Image')], default='text', max_length=200, verbose_name='Type'),
        ),
    ]