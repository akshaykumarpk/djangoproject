# Generated by Django 4.1.2 on 2023-01-12 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imagename', models.CharField(max_length=30)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('Model', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
