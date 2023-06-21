from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        validators=[
            MinValueValidator(12),
        ],
        blank=False,
        null=False,
    )
    password = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )
    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    profile_picture = models.URLField(
        blank=False,
        null=False,
    )

    @property
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return ''


class Game(models.Model):
    title = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        unique=True,
    )
    category = models.CharField(
        max_length=15,
        choices=[
            ("Action", "Action"),
            ("Adventure", "Adventure"),
            ("Puzzle", "Puzzle"),
            ("Strategy", "Strategy"),
            ("Sports", "Sports"),
            ("Board/Card Game", "Board/Card Game"),
            ("Other", "Other"),
        ],
        blank=False,
        null=False,
    )
    rating = models.FloatField(
        validators=[
            MinValueValidator(0.1),
            MaxValueValidator(5.0),
        ]
    )
    max_level = models.IntegerField(
        validators=[
            MinValueValidator(1),
        ],
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        blank=False,
        null=False,
    )
    summary = models.TextField(
        blank=True,
        null=True,
    )
