# Generated by Django 4.0.6 on 2022-07-30 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_reservebook_expiredate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservebook',
            old_name='bookID',
            new_name='book',
        ),
    ]