# Generated by Django 5.0.4 on 2024-05-07 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_jobapplication_jobpostid_jobapplication_userapplied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='ApplyDate',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
