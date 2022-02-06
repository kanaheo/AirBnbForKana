import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):
    help = "This command creates many rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many rooms?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 5),
                "price": lambda x: random.randint(1, 300000),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "bathrooms": lambda x: random.randint(1, 5),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(
            list(created_photos.values())
        )  # 위에서 execute한 포토의 pk들( faltten으로 예쁘게 정리)
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()
        for pk in created_clean:  # 생성된 모든 룸으로 for문 !
            room = room_models.Room.objects.get(pk=pk)  # pk로 방을 찾기 !
            for i in range(3, random.randint(10, 30)):  # 사진을 최소,3, 최대 17까지 생성한다
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"/room_photos/{random.randint(1, 31)}.webp",
                )
            for a in amenities:  # 다대다 필드에서 무언가를 추가하는방법
                magin_number = random.randint(0, 15)
                if magin_number % 2 == 0:  # <- 이 부분에서 % 2 == 0 이면
                    room.amenities.add(a)
            for f in facilities:  # 다대다 필드에서 무언가를 추가하는방법
                magin_number = random.randint(0, 15)
                if magin_number % 2 == 0:  # <- 이 부분에서 % 2 == 0 이면
                    room.facilities.add(f)
            for r in rules:  # 다대다 필드에서 무언가를 추가하는방법
                magin_number = random.randint(0, 15)
                if magin_number % 2 == 0:  # <- 이 부분에서 % 2 == 0 이면
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
