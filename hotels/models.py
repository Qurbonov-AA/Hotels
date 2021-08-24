from django.db import models
import datetime
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)


class Hotels(models.Model):
    hotel_name = models.CharField(max_length=150)      # hotel name
    date = models.DateField(default=today)            # 30.06.2021
    phone = models.CharField(max_length=13)            # +998123456789
    email = models.EmailField()                        # hotel@hotel.uz
    adress_text = models.CharField(
        max_length=120)     # I.Karimov ko`chasi 74/2
    # 40.11732598234071, 65.35481219380598
    adress_google = models.CharField(max_length=50)
    star_rate = models.FloatField(default=1)
    info = models.TextField(default="")

    Bar = models.BooleanField(default=False)
    Fitnes_Club = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Гостиница"
        verbose_name_plural = "1.Гостиницы"

    def __str__(self):
        return str(self.hotel_name)


# class Services(models.Model):
#     hotel = models.ForeignKey(Hotels, on_delete= models.CASCADE)
#     name  = models.CharField(max_length=150)            # hotel name
#     dates = models.DateField(default= datetime.today()) # 30.06.2021
#     class Meta:
#         verbose_name        = "Сервис"
#         verbose_name_plural = "2.Сервисы"

#     def __str__(self):
#         return self.name


class Rooms(models.Model):
    quality = (
        ("1", "Одноместный"),
        ("2", "Двухместный"),
        ("3", "Трёхместный"),
        ("4", "Четерёхместный"),
    )
    types = (
        ("default", "Обычный"),
        ("lux", "Люкс"),
    )
    #hotel = models.ForeignKey(Services, on_delete= models.CASCADE)
    room = models.ForeignKey(
        Hotels, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    quantity_room = models.CharField(max_length=20, choices=quality)
    type_room = models.CharField(max_length=10, choices=types)

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "3.Номера"

    def __str__(self):
        return str(self.room) + " -> " + str(self.quantity_room) + " -> " + str(self.type_room)


class description_list(models.Model):
    description = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    tv = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    refrigerator = models.BooleanField(default=False)
    radio = models.BooleanField(default=False)
    sauna = models.BooleanField(default=False)
    Extra_long_beds = models.BooleanField(default=False)
    Walk_in_closet = models.BooleanField(default=False)

    Baby_safety_gates = models.BooleanField(default=False)
    Desk = models.BooleanField(default=False)
    Clothes_rack = models.BooleanField(default=False)
    Heating = models.BooleanField(default=False)
    Board_games_puzzles = models.BooleanField(default=False)
    Iron = models.BooleanField(default=False)

    #photo = models.ImageField(storage=fs)

    class Meta:
        verbose_name = "Описание номер"
        verbose_name_plural = "4.Описании номера"

    def __str__(self):
        return str(self.description)


class Guests(models.Model):
    hotel_name_number = models.ForeignKey(
        description_list, on_delete=models.CASCADE)
    date_from = models.DateField(default=today)
    date_to = models.DateField(default=tomorrow)
    FirstName = models.CharField(default="", max_length=40)

    LastName = models.CharField(default="", max_length=40)
    Passport_Serial = models.CharField(max_length=4, default="AA")
    Passport_Number = models.IntegerField(max_length=10, default=1234567)

    class Meta:
        verbose_name = "Госты"
        verbose_name_plural = "5.ФИО Госты"

    def __str__(self):
        return str(self.FirstName) + " " + str(self.LastName)
