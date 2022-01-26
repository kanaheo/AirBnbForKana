from django.db import models


class AbstractTimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # 추상적인 ! 데이터베이스에는 직접 등록이 안되게 한다. 상속시켜서 사용은 가능함
