# Generated by Django 2.1.5 on 2019-04-09 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_stash', '0005_auto_20190407_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='belonged_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owned_parts_ITEMLIST', to='my_stash.Itemset'),
        ),
    ]
