# Generated by Django 5.0.4 on 2024-05-05 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_userprofile_certifications_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='certifications',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='cv/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='education',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='work_experience',
            field=models.TextField(blank=True, null=True),
        ),
    ]
