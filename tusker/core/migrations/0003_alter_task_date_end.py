# Generated by Django 4.1.4 on 2022-12-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_task_task_description_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_end',
            field=models.DateField(null=True),
        ),
    ]
