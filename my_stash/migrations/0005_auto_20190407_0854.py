# Generated by Django 2.1.5 on 2019-04-06 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_stash', '0004_auto_20190407_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemset',
            name='is_myth',
        ),
        migrations.AddField(
            model_name='itemset',
            name='is_lv94',
            field=models.BooleanField(default=True, verbose_name='要求レベル94'),
        ),
    ]
