# Generated by Django 3.1.6 on 2021-02-12 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0002_auto_20210212_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='region',
            field=models.CharField(blank=True, choices=[('america', 'Americas'), ('europe', 'Europe'), ('africa', 'Africa'), ('asia', 'Asia'), ('oceania', 'Oceania')], max_length=100, null=True),
        ),
    ]
