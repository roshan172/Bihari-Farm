# Generated by Django 2.2.7 on 2019-12-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmsite', '0005_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='designation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
