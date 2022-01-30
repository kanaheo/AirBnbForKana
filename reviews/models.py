from django.db import models
from core import models as core_models


class Review(core_models.AbstractTimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    accuracy = models.IntegerField()  # 정확성
    communication = models.IntegerField()  # 의사소통
    cleanliness = models.IntegerField()  # 청결도
    Location = models.IntegerField()  # 위치
    check_in = models.IntegerField()  # 체크인
    value = models.IntegerField()  # 가격 대비 만족도
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )  # 유저를 삭제하면 관련 리뷰도 삭제 !
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )  # 방을 삭제해도 관련 리뷰 삭제 !

    def __str__(self):
        return f"{self.review} - {self.room}"
