# Generated by Django 2.1.7 on 2019-02-17 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wineapp', '0002_auto_20190217_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='country',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='designaion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='points',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='price',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='province',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='variety',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='winery',
            field=models.TextField(null=True),
        ),
    ]
