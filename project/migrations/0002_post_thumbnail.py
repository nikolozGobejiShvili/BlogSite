# Generated by Django 4.0.3 on 2022-04-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='exit', upload_to='project/post_thumbnail/'),
            preserve_default=False,
        ),
    ]