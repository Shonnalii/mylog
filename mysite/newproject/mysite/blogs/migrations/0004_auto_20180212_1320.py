# Generated by Django 2.0.1 on 2018-02-12 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20180212_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogtag',
            name='tag',
        ),
        migrations.AddField(
            model_name='blogtag',
            name='blog_tag',
            field=models.OneToOneField(default=1, on_delete=1, to='blogs.Tag'),
            preserve_default=False,
        ),
    ]
