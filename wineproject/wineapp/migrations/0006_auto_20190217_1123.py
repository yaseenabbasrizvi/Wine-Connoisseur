# Generated by Django 2.1.7 on 2019-02-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wineapp', '0005_auto_20190217_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='country',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='designaion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='province',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='region_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='region_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='variety',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='winery',
            field=models.TextField(blank=True, null=True),
        ),
    ]
