# Generated by Django 4.0.4 on 2022-04-19 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_student_shift_student_subjects_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='complaint',
            new_name='message',
        ),
    ]
