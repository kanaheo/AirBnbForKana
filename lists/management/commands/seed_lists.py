import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models

NAME = "lists"


class Command(BaseCommand):
    help = f"This command creates many {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help=f"How many {NAME}?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        # rooms = room_models.Room.objects.all()[4:10]  # <- 4~10번까지의 방만가지고옴
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            list_models.List,
            number,
            {
                "user": lambda x: random.choice(users),
            },
        )
        created = seeder.execute()
        cleaned = flatten(list(created.values()))

        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add_room = rooms[random.randint(0, 5) : random.randint(6, 30)]
            # list_model.rooms.add(to_add_room) # 이렇게 되면 list_model가 array가 된다고 하는군 !
            list_model.rooms.add(*to_add_room)  # 이렇게 하면 array안에 있는 요소만 가지고옴

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
