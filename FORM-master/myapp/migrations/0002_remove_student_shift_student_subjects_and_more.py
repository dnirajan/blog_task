# Generated by Django 4.0.4 on 2022-04-18 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='shift',
        ),
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='complaint',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=None, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.PositiveIntegerField(default=0),
        ),
    ]