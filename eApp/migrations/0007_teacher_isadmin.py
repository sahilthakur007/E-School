# Generated by Django 4.1.1 on 2022-10-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eApp', '0006_student_prn_student_identity_student_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='isadmin',
            field=models.BooleanField(default=False),
        ),
    ]
