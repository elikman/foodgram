# Generated by Django 3.2.3 on 2024-09-28 19:20

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodgramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('avatar', models.ImageField(blank=True, default=None, null=True, upload_to='users/')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('-date_joined', 'username'),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_to_shopping', to='recipes.recipe', verbose_name='рецепт')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_to_user', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'подписка',
                'verbose_name_plural': 'Подписки',
                'ordering': ('user', 'recipe'),
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='подписчик')),
            ],
            options={
                'verbose_name': 'подписка',
                'verbose_name_plural': 'Подписки',
                'ordering': ('author', 'user'),
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_to_favorite', to='recipes.recipe', verbose_name='рецепт')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_to_user', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'ordering': ('user', 'recipe'),
            },
        ),
        migrations.AddField(
            model_name='foodgramuser',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorite', through='users.Favorite', to='recipes.Recipe', verbose_name='Избранное'),
        ),
        migrations.AddField(
            model_name='foodgramuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='foodgramuser',
            name='shopping_cart',
            field=models.ManyToManyField(blank=True, related_name='shopping', through='users.ShoppingCart', to='recipes.Recipe', verbose_name='Список покупок'),
        ),
        migrations.AddField(
            model_name='foodgramuser',
            name='subscriptions',
            field=models.ManyToManyField(blank=True, related_name='followers', through='users.Follow', to=settings.AUTH_USER_MODEL, verbose_name='Подписки'),
        ),
        migrations.AddField(
            model_name='foodgramuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddConstraint(
            model_name='shoppingcart',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='unique_shopping'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'author'), name='unique_user_following'),
        ),
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='unique_favorite'),
        ),
    ]
