# Generated by Django 4.2.9 on 2024-01-28 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='verify_code',
        ),
        migrations.AddField(
            model_name='user',
            name='chat_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='ID чата'),
        ),
        migrations.AddField(
            model_name='user',
            name='telegram',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='ник в телеграме'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]