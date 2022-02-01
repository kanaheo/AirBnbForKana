from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    # 진짜 어드민 패널에 뿌려주는것 ! fieldsets
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "beths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenity", "facility", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "price",
        "city",
        "guests",
        "beds",
        "bedrooms",
        "beths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    ordering = ("name", "price", "bedrooms")

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenity",
        "facility",
        "house_rules",
        "city",
        "country",
    )

    search_fields = ("=city", "^host__username")

    filter_horizontal = (  # many to relationships에서 사용한다
        "amenity",
        "facility",
        "house_rules",
    )

    # self는 RoomAdmin클래스, obj는 room의 row( 즉 a라는 room) 여기에 잇는 amentities를 count하기위해
    def count_amenities(self, obj):
        return obj.amenity.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    pass
