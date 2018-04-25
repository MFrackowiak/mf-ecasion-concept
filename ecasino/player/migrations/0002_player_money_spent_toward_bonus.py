# Generated by Django 2.0.4 on 2018-04-24 14:28

import common.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='money_spent_toward_bonus',
            field=common.fields.MoneyField(decimal_places=2, default=0, max_digits=10),
        ),
    ]