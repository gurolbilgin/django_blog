# Generated by Django 3.2.5 on 2021-10-26 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Some Awesome Blogpost!!!', max_length=20),
        ),
    ]
