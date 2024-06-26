# Generated by Django 5.0.3 on 2024-04-12 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=255)),
                ('EMAIL', models.EmailField(max_length=254)),
                ('SUBJECT', models.TextField(max_length=1024)),
                ('SUBMITED_DATE', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Index_work_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_img', models.ImageField(upload_to='index_works_page')),
                ('work_name', models.CharField(default='...', max_length=255)),
                ('work_dis', models.CharField(default='...', max_length=255)),
                ('work_url', models.CharField(default='#', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_url', models.CharField(default='#', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Work_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_image', models.ImageField(upload_to='works_page')),
                ('work_names', models.CharField(default='...', max_length=255)),
                ('work_diss', models.CharField(default='...', max_length=255)),
                ('work_urls', models.CharField(default='#', max_length=255)),
                ('work_main_diss', models.CharField(default='...', max_length=1024)),
            ],
        ),
    ]
