# Generated by Django 3.2 on 2021-04-13 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gally', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='img_category',
            field=models.CharField(choices=[('TRAVEL', 'TRAVEL'), ('PARTIES', 'PARTIES')], default='PARTIES', max_length=100),
        ),
    ]
