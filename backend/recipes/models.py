from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from common.constants import MAX_32, MAX_64, MAX_128, MAX_256

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=MAX_32, verbose_name='Название')
    slug = models.SlugField(
        max_length=MAX_32, verbose_name='Слаг', unique=True,
        error_messages={'unique': 'Такой слаг уже существует.'}
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['name']

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_128
    )
    measurement_unit = models.CharField(
        verbose_name='Единица измерения',
        max_length=MAX_64
    )

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'measurement_unit'],
                name='unique_name_measurement_unit'
            )
        ]

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class IngredientsRecipes(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField(
        verbose_name='Количество игридиента',
        validators=[MinValueValidator(1)],
        error_messages={
            'amount': 'Значение должно быть больш 0.'}
    )

    class Meta:
        default_related_name = 'recipe_ingredients'
        verbose_name = 'Ингридиенты в рецепте'
        verbose_name_plural = 'Ингридиенты в рецептах'
        ordering = ['recipe', 'ingredient']

    def __str__(self):
        return f'{self.ingredient} в {self.recipe}'


class RecipeQuerySet(models.QuerySet):

    def with_related_data(self):
        return self.select_related('author')

    def with_prefetch_data(self):
        return self.prefetch_related('tags', 'ingredients')


class RecipeManager(models.Manager):

    def get_queryset(self):
        return (
            RecipeQuerySet(self.model)
            .with_related_data()
            .with_prefetch_data()
        )


class Recipe(models.Model):
    ingredients = models.ManyToManyField(
        Ingredient,
        through=IngredientsRecipes,
    )
    tags = models.ManyToManyField(
        Tag,
        through='TagsRecipes',
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='recipes/images/',
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_256,
    )
    text = models.TextField(verbose_name='Описание')
    cooking_time = models.IntegerField(
        verbose_name='Время приготовления (мин.)',
        validators=[MinValueValidator(1)]
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор рецепта',
    )
    short_link = models.CharField(
        verbose_name='Короткая ссылка',
        max_length=10,
        unique=True
    )
    objects = models.Manager()
    with_related = RecipeManager()

    class Meta:
        default_related_name = 'recipes'
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'name'],
                name='unique_author_name'
            )
        ]

    def __str__(self):
        return self.name


class TagsRecipes(models.Model):
    tag = models.ForeignKey(
        Tag, on_delete=models.SET_NULL, null=True
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'recipe_tags'
        verbose_name = 'Теги рецепта'
        verbose_name_plural = 'Теги рецептов'
        ordering = ['recipe', 'tag']
        constraints = [
            models.UniqueConstraint(
                fields=['tag', 'recipe'],
                name='unique_tag_recipe'
            )
        ]

    def __str__(self):
        return f"{self.tag} в {self.recipe}"


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'shopping_cart'
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'
        ordering = ['user', 'recipe']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_shopping_cart_user_recipe'
            )
        ]

    def __str__(self):
        return f"{self.user}'s shopping cart: {self.recipe}"


class FavoriteRecipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'favorite_recipes'
        verbose_name = 'Избранный рецепт'
        verbose_name_plural = 'Избранные рецепты'
        ordering = ['user', 'recipe']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_favorites_user_recipe'
            )
        ]

    def __str__(self):
        return f"{self.user}'s favorite: {self.recipe}"
