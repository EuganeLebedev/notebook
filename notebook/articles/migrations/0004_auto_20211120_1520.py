# Generated by Django 3.2.9 on 2021-11-20 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_post_categoryes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoryes',
            field=models.ManyToManyField(related_name='Categoryes', to='articles.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Заголовок'),
        ),
    ]
