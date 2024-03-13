# Generated by Django 5.0.3 on 2024-03-13 10:46

import django.db.models.deletion
import django_resized.forms
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "Countries",
            },
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=20)),
                ("image", models.FileField(blank=True, null=True, upload_to="icons/")),
                ("slug", models.SlugField(max_length=20, unique=True)),
            ],
            options={
                "verbose_name_plural": "Tags",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("body", models.CharField(max_length=600)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="LikedComment",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="a_plot.comment"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="comment",
            name="likes",
            field=models.ManyToManyField(
                related_name="likedcomments",
                through="a_plot.LikedComment",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="LikedPlot",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Plot",
            fields=[
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "season",
                    models.CharField(
                        blank=True,
                        choices=[("Low", "Low"), ("Mid", "Mid"), ("High", "High")],
                        default="Mid",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "plot_image",
                    django_resized.forms.ResizedImageField(
                        blank=True,
                        crop=None,
                        force_format=None,
                        keep_meta=True,
                        null=True,
                        quality=85,
                        scale=None,
                        size=[600, 600],
                        upload_to="photos/",
                    ),
                ),
                ("plot", models.CharField(max_length=100)),
                (
                    "categories",
                    models.CharField(
                        choices=[
                            ("Campsite", "Campsite"),
                            ("Official", "Official"),
                            ("Wild", "Wild"),
                        ],
                        default=1,
                        max_length=25,
                    ),
                ),
                ("what3words", models.URLField(blank=True, null=True)),
                ("campsite", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "countries",
                    models.CharField(
                        choices=[
                            ("Spain", "Spain"),
                            ("France", "France"),
                            ("Portugal", "Portugal"),
                            ("Italy", "Italy"),
                            ("Germany", "Germany"),
                            ("Netherlands", "Netherlands"),
                            ("Belgium", "Belgium"),
                            ("Switzerland", "Switzerland"),
                            ("Sweden", "Sweden"),
                            ("Norway", "Norway"),
                            ("Finland", "Finland"),
                            ("Denmark", "Denmark"),
                            ("Ireland", "Ireland"),
                            ("United Kingdom", "United Kingdom"),
                            ("Austria", "Austria"),
                            ("Greece", "Greece"),
                            ("Croatia", "Croatia"),
                            ("Poland", "Poland"),
                            ("Romania", "Romania"),
                            ("Bulgaria", "Bulgaria"),
                            ("Czech Republic", "Czech Republic"),
                            ("Hungary", "Hungary"),
                            ("Slovakia", "Slovakia"),
                            ("Slovenia", "Slovenia"),
                            ("Luxembourg", "Luxembourg"),
                            ("Latvia", "Latvia"),
                            ("Estonia", "Estonia"),
                            ("Lithuania", "Lithuania"),
                            ("Malta", "Malta"),
                            ("Cyprus", "Cyprus"),
                            ("Iceland", "Iceland"),
                            ("Liechtenstein", "Liechtenstein"),
                            ("Monaco", "Monaco"),
                            ("San Marino", "San Marino"),
                            ("Andorra", "Andorra"),
                            ("Albania", "Albania"),
                            ("Armenia", "Armenia"),
                            ("Azerbaijan", "Azerbaijan"),
                            ("Belarus", "Belarus"),
                            ("Bosnia and Herzegovina", "Bosnia and Herzegovina"),
                            ("Georgia", "Georgia"),
                            ("Kazakhstan", "Kazakhstan"),
                            ("Kosovo", "Kosovo"),
                            ("Macedonia", "Macedonia"),
                            ("Moldova", "Moldova"),
                            ("Montenegro", "Montenegro"),
                            ("Russia", "Russia"),
                            ("Serbia", "Serbia"),
                            ("Turkey", "Turkey"),
                            ("Ukraine", "Ukraine"),
                        ],
                        default="Spain",
                        max_length=100,
                    ),
                ),
                ("list_date", models.DateTimeField(auto_now_add=True)),
                ("approved", models.BooleanField(default=True)),
                (
                    "reported_by",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "reason",
                    models.CharField(
                        choices=[
                            ("Off Topic", "Off Topic"),
                            ("Spam", "Spam"),
                            ("Sexual content", "Sexual content"),
                            ("Nudity", "Nudity"),
                            ("Breaks Rules", "Breaks Rules"),
                            ("Other", "Other"),
                        ],
                        default="Off Topic",
                        max_length=100,
                    ),
                ),
                ("reported_date", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        related_name="likedplots",
                        through="a_plot.LikedPlot",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="plots",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-list_date"],
            },
        ),
        migrations.AddField(
            model_name="likedplot",
            name="plot",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="a_plot.plot"
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="parent_plot",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="a_plot.plot",
            ),
        ),
        migrations.CreateModel(
            name="Reply",
            fields=[
                ("body", models.CharField(max_length=150)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="replies",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "parent_comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="replies",
                        to="a_plot.comment",
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
            },
        ),
    ]
