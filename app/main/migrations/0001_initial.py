# Generated by Django 4.1.1 on 2023-01-22 10:49

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
from django.contrib.auth.validators import UnicodeUsernameValidator
import django.utils.timezone
import easy_thumbnails.fields
import main.utilities


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdvUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "password",
                    models.CharField(max_length=128, verbose_name="password"),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all "
                        + "permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that "
                            + "username already exists."
                        },
                        help_text="Required. 150 characters or fewer. "
                        + "Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[UnicodeUsernameValidator()],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        verbose_name="email address",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be "
                        + "treated as active. Unselect this instead "
                        + "of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="date joined",
                    ),
                ),
                (
                    "is_activated",
                    models.BooleanField(
                        db_index=True,
                        default=True,
                        verbose_name="Прошел активацию?",
                    ),
                ),
                ("is_staff", models.BooleanField(default=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. "
                        + "A user will get all permissions granted "
                        + "to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        max_length=28,
                        unique=True,
                        verbose_name="Название",
                    ),
                ),
                (
                    "cover",
                    easy_thumbnails.fields.ThumbnailerImageField(
                        blank=True,
                        null=True,
                        upload_to=main.utilities.get_timestamp_path,
                        verbose_name="1024 x 272",
                    ),
                ),
            ],
            options={
                "verbose_name": "Музыкальный стиль",
                "verbose_name_plural": " Музыкальные стили",
            },
        ),
        migrations.CreateModel(
            name="Pgm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "num",
                    models.CharField(
                        db_index=True,
                        max_length=4,
                        unique=True,
                        verbose_name="Номер",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        max_length=48,
                        unique=True,
                        verbose_name="Название",
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        db_index=True,
                        unique=True,
                        verbose_name="Дата выхода в эфир",
                    ),
                ),
                (
                    "note",
                    models.CharField(
                        db_index=True,
                        max_length=177,
                        verbose_name="Описание программы",
                    ),
                ),
                (
                    "intro",
                    models.TextField(verbose_name="Вступительное слово"),
                ),
                (
                    "cover",
                    easy_thumbnails.fields.ThumbnailerImageField(
                        blank=True,
                        null=True,
                        upload_to=main.utilities.get_timestamp_path,
                        verbose_name="1024 x 272",
                    ),
                ),
                ("genres", models.ManyToManyField(to="main.genre")),
            ],
            options={
                "verbose_name": "Программа",
                "verbose_name_plural": " Программы",
                "ordering": ("-num",),
            },
        ),
        migrations.CreateModel(
            name="Playlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pos",
                    models.PositiveIntegerField(
                        db_index=True, default=0, verbose_name="Номер"
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=53, verbose_name="Название"),
                ),
                (
                    "note",
                    models.CharField(
                        blank=True,
                        max_length=177,
                        null=True,
                        verbose_name="Описание",
                    ),
                ),
                (
                    "intro",
                    models.TextField(
                        blank=True, null=True, verbose_name="Вступление"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        verbose_name="Опубликован",
                    ),
                ),
                (
                    "favs",
                    models.ManyToManyField(
                        related_name="liked_playlists",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Плейлист",
                "verbose_name_plural": "Мои плейлисты",
                "ordering": ["pos"],
            },
        ),
        migrations.CreateModel(
            name="Rubric",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        max_length=25,
                        unique=True,
                        verbose_name="Название",
                    ),
                ),
                (
                    "note",
                    models.CharField(
                        blank=True,
                        max_length=40,
                        null=True,
                        unique=True,
                        verbose_name="Описание",
                    ),
                ),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={
                "ordering": ("order",),
            },
        ),
        migrations.CreateModel(
            name="Track",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pos",
                    models.SmallIntegerField(
                        db_index=True, verbose_name="Трек"
                    ),
                ),
                (
                    "artist",
                    models.CharField(
                        db_index=True,
                        max_length=77,
                        verbose_name="Исполнитель",
                    ),
                ),
                (
                    "album",
                    models.CharField(
                        db_index=True, max_length=103, verbose_name="Альбом"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_index=True, max_length=93, verbose_name="Название"
                    ),
                ),
                (
                    "label",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=51,
                        null=True,
                        verbose_name="Лейбл",
                    ),
                ),
                (
                    "duration",
                    models.SmallIntegerField(
                        db_index=True, verbose_name="Длительность, сек."
                    ),
                ),
                (
                    "is_free",
                    models.BooleanField(
                        db_index=True, default=False, verbose_name="Free"
                    ),
                ),
                (
                    "year",
                    models.SmallIntegerField(
                        blank=True,
                        db_index=True,
                        null=True,
                        verbose_name="Год",
                    ),
                ),
                (
                    "cover",
                    easy_thumbnails.fields.ThumbnailerImageField(
                        blank=True,
                        null=True,
                        upload_to="",
                        verbose_name="1 x 1, png",
                    ),
                ),
                (
                    "pgm",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="main.pgm",
                        verbose_name="Программа",
                    ),
                ),
            ],
            options={
                "verbose_name": "Трек программы",
                "verbose_name_plural": " Треки программ",
                "ordering": ("-pgm__num", "pos"),
            },
        ),
        migrations.CreateModel(
            name="PlaylistTracks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("track_order", models.PositiveIntegerField(default=0)),
                (
                    "playlist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.playlist",
                    ),
                ),
                (
                    "track",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.track",
                    ),
                ),
            ],
            options={
                "verbose_name": "Трек",
                "verbose_name_plural": "Треки",
                "ordering": ["track_order"],
            },
        ),
        migrations.AddField(
            model_name="playlist",
            name="tracks",
            field=models.ManyToManyField(
                through="main.PlaylistTracks", to="main.track"
            ),
        ),
        migrations.AddField(
            model_name="playlist",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.CreateModel(
            name="SubRubric",
            fields=[],
            options={
                "verbose_name": "Подрубрика",
                "verbose_name_plural": "Подрубрики",
                "ordering": ("super_rubric__order", "order"),
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("main.rubric",),
        ),
        migrations.CreateModel(
            name="SuperRubric",
            fields=[],
            options={
                "verbose_name": "Надрубрика",
                "verbose_name_plural": "Надрубрики",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("main.rubric",),
        ),
        migrations.AddField(
            model_name="rubric",
            name="super_rubric",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="main.superrubric",
                verbose_name="Надрубрика",
            ),
        ),
        migrations.AddField(
            model_name="playlist",
            name="subrubric",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="main.subrubric",
                verbose_name="Подрубрика",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="playlist",
            unique_together={("user", "name")},
        ),
        migrations.AlterIndexTogether(
            name="playlist",
            index_together={("user", "name")},
        ),
    ]
