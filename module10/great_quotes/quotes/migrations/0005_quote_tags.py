# Generated by Django 5.0.6 on 2024-05-14 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0004_remove_quote_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='tags',
            field=models.ManyToManyField(to='quotes.tag'),
        ),
    ]
