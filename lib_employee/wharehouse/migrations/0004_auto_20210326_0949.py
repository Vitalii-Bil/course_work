# Generated by Django 3.1.7 on 2021-03-26 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wharehouse', '0003_auto_20210326_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wharehouse.book', verbose_name='book'),
        ),
    ]
