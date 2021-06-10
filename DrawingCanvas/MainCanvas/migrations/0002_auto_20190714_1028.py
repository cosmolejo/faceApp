# Generated by Django 2.1.5 on 2019-07-14 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainCanvas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drawing',
            name='circles',
        ),
        migrations.RemoveField(
            model_name='drawing',
            name='lines',
        ),
        migrations.AddField(
            model_name='drawing',
            name='drawingJSONText',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='Circle',
        ),
        migrations.DeleteModel(
            name='Line',
        ),
    ]
