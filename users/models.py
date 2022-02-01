from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):

    """전체적으로 Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    """ CharField에서 select문처럼 옵션추가하는거 비슷한거"""
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREA = "kr"
    # LANGUAGE_CHOICES = (
    #     (LANGUAGE_ENGLISH, "English"),
    #     (LANGUAGE_KOREA, "Korea")
    #     (db의 value, 유저가 보는 )
    # )
    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREA, "Korea"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    # bio = models.TextField(null=True)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthday = models.DateField(
        help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
        blank=True,
        null=True,
    )
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)

    superhost = models.BooleanField(default=False)
