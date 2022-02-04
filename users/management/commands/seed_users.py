from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):
    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many users?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        # 밑에는 ! user를 만들건데 ! 만들 때 is_staff 가 아니고 superhost가 아닌걸로 일반 유저로 만들기 !! 즉 커스터마이즈
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))
