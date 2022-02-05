from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = "This command let's go ! "

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="This command creates facilities",
        )

    def handle(self, *args, **options):
        # print(args, options)  확인해보고싶으면 확인해보기 ~
        # print("i love you")
        # times = options.get("times")  # str이니 ..밑에서 int로
        # for t in range(0, int(times)):
        #     self.stdout.write(self.style.SUCCESS('times'))

        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for facility in facilities:
            Facility.objects.create(name=facility)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created!"))
