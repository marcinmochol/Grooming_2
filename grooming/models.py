from django.db import models
from django.utils import timezone

class DogService(models.Model):
    name_choice = (
    (1, "Kąpiel"),
    (2, "Strzyżenie"),
    (3, "Trymowanie"),
    (4, "Mycie zębów"),
    (5,"Podcinanie pazurów")
)
    service_name = models.IntegerField(choices=name_choice, verbose_name='Nawza usługi')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Cena')

    def __str__(self):
        return self.service_name

class DogReservation(models.Model):
    dog_name = models.CharField(max_length=64, verbose_name='Imię psa')
    phone_number = models.CharField(max_length=20, verbose_name='Numer telefonu właściciela')
    comment = models.TextField(null=True, verbose_name='Komentarz')
    reservation_time = models.DateTimeField(verbose_name='Czas rezerwacji')
    STATUS_CHOICES = [
        ('scheduled', 'Zaplanowana'),
        ('completed', 'Zakończona'),
        ('cancelled', 'Anulowana'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='scheduled',
        verbose_name='Status'
    )
    services = models.ManyToManyField(DogService, related_name='dog_reservations', verbose_name='Usługi')
    def __str__(self):
        return f"Rezerwacja dla {self.dog_name} - {self.reservation_time}"

    def is_upcoming(self):
        return self.reservation_time > timezone.now()

    def is_past(self):
        return self.reservation_time < timezone.now()
    
