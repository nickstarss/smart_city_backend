# Generated by Django 5.0.3 on 2024-06-03 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_smart', '0003_alter_temperaturadata_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luminosidadedata',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
