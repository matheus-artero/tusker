# Generated by Django 4.1.4 on 2022-12-30 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('O', 'open'), ('P', 'in progress'), ('C', 'closed')], max_length=1),
        ),
    ]
