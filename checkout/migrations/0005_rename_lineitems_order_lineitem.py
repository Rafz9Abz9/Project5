# Generated by Django 5.0.1 on 2024-02-25 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_rename_line_items_order_lineitems'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='lineitems',
            new_name='lineitem',
        ),
    ]