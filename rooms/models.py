from tabnanny import verbose
from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# 아이템을 가질 때 ! ( room이 특별하게 뭔가 옵션을 가질 때? 그런데 처음에 migrate에는 영향안가게 필요할 때 사용하게 )
class AbstractItem(core_models.AbstractTimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """RoomType Object Definition"""

    class Meta:
        verbose_name = "Room Type"


# 편의시설
class Amenity(AbstractItem):

    """Amenity Object Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


# 이용시설
class Facility(AbstractItem):

    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """HouseRule Model Definition"""

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.AbstractTimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)  # 설명
    file = models.ImageField()
    room = models.ForeignKey(
        "Room", related_name="photos", on_delete=models.CASCADE
    )  # room을 지우면 이미지도 지워야지 !

    def __str__(self):
        return self.caption


# core models에서 models를 상속받고 잇으니 그대로 밑에 써도 괜찮 !
# 여기가 admin페이지에서 보여주는것같음
class Room(core_models.AbstractTimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    price = models.IntegerField()
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    beths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    # SET_NULL : 값이 사라진다면 ForeignKeyField이 null로 바뀐다.(null=True필수)
    # roomtype는 1개여야만한다. airbnb 참고, 또한 room_type가 삭제된다고 room이 삭제되면 이상해 !
    amenity = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facility = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name
