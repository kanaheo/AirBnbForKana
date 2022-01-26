from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

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

    pass


# 편의시설
class Amenity(AbstractItem):

    """Amenity Object Definition"""

    pass


# 편의시설
class Facility(AbstractItem):

    """Facility Model Definition"""

    pass


class HouseRule(AbstractItem):

    """HouseRule Model Definition"""

    pass


# core models에서 models를 상속받고 잇으니 그대로 밑에 써도 괜찮 !
class Room(core_models.AbstractTimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    beths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    # SET_NULL : 값이 사라진다면 ForeignKeyField이 null로 바뀐다.(null=True필수)
    # roomtype는 1개여야만한다. airbnb 참고, 또한 room_type가 삭제된다고 room이 삭제되면 이상해 !
    amenity = models.ManyToManyField(Amenity)
    facility = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)

    def __str__(self):
        return self.name
