from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    help = "This command let's go ! "

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="This command creates amenities",
        )

    def handle(self, *args, **options):
        # print(args, options)  확인해보고싶으면 확인해보기 ~
        # print("i love you")
        # times = options.get("times")  # str이니 ..밑에서 int로
        # for t in range(0, int(times)):
        #     self.stdout.write(self.style.SUCCESS('times'))

        amenities = [
            "Air conditioning",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Bed Linen",
            "Boating",
            "Cable TV",
            "Carbon monoxide detectors",
            "Chairs",
            "Children Area",
            "Coffee Maker in Room",
            "Cooking hob",
            "Cookware & Kitchen Utensils",
            "Dishwasher",
            "Double bed",
            "En suite bathroom",
            "Free Parking",
            "Free Wireless Internet",
            "Freezer",
            "Fridge / Freezer",
            "Golf",
            "Hair Dryer",
            "Heating",
            "Hot tub",
            "Indoor Pool",
            "Ironing Board",
            "Microwave",
            "Outdoor Pool",
            "Outdoor Tennis",
            "Oven",
            "Queen size bed",
            "Restaurant",
            "Shopping Mall",
            "Shower",
            "Smoke detectors",
            "Sofa",
            "Stereo",
            "Swimming pool",
            "Toilet",
            "Towels",
            "TV",
        ]

        for amenity in amenities:
            Amenity.objects.create(name=amenity)
        self.stdout.write(self.style.SUCCESS("Amenity created!"))
