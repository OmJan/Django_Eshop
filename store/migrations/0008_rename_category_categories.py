# Generated by Django 4.2.5 on 2023-10-07 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_order_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categories',
        ),
    ]
