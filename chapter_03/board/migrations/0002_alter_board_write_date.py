# Generated by Django 4.2 on 2023-04-13 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='write_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='작성일자'),
        ),
    ]
