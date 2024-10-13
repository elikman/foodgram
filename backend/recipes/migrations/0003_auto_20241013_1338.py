# Generated by Django 3.2.3 on 2024-10-13 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favoriterecipes',
            options={'default_related_name': 'favorite_recipes', 'ordering': ['user', 'recipe'], 'verbose_name': 'Избранный рецепт', 'verbose_name_plural': 'Избранные рецепты'},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name'], 'verbose_name': 'Ингридиент', 'verbose_name_plural': 'Ингридиенты'},
        ),
        migrations.AlterModelOptions(
            name='ingredientsrecipes',
            options={'default_related_name': 'recipe_ingredients', 'ordering': ['recipe', 'ingredient'], 'verbose_name': 'Ингридиенты в рецепте', 'verbose_name_plural': 'Ингридиенты в рецептах'},
        ),
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'default_related_name': 'shopping_cart', 'ordering': ['user', 'recipe'], 'verbose_name': 'Список покупок', 'verbose_name_plural': 'Списки покупок'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
        migrations.AlterModelOptions(
            name='tagsrecipes',
            options={'default_related_name': 'recipe_tags', 'ordering': ['recipe', 'tag'], 'verbose_name': 'Теги рецепта', 'verbose_name_plural': 'Теги рецептов'},
        ),
    ]