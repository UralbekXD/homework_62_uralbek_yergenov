# Generated by Django 4.1.6 on 2023-03-21 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0003_alter_project_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': [('manage_project_tasks', 'Редактировать задачи проекта')]},
        ),
    ]
