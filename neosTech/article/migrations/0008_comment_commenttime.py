# Generated by Django 4.2.1 on 2023-09-03 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_comment_productcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentTime',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name=''),
        ),
    ]
