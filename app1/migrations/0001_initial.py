# Generated by Django 2.1.5 on 2020-09-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_Name', models.CharField(max_length=45)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=10)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('mobile_No', models.CharField(max_length=11, unique=True)),
                ('date_of_Birth', models.DateField()),
                ('university_Name', models.CharField(choices=[('bau', 'Bangladesh Agricultural University'), ('hstu', 'Hajee Mohammad Danesh Science and Technology University'), ('ku', 'Khulna University'), ('nstu', 'Noakhali Science and Technology University'), ('pstu', 'Patuakhali Science & Technology University'), ('ru', 'University of Rajshahi'), ('sbau', 'Sher-e-Bangla Agricultural University'), ('sau', 'Sylhet Agricultural University'), ('others', 'Others')], max_length=100)),
                ('picture', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]
