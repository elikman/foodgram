# Generated by Django 3.2.3 on 2024-10-01 20:59

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='short_link',
            field=shortuuid.django_fields.ShortUUIDField(alphabet=None, length=10, max_length=10, prefix='', unique=True),
        ),
    ]
