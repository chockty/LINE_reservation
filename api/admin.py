from django.contrib import admin

# Register your models here.
from .models import User
from .models import Reservation
from .models import ReservationsChoice

admin.site.register(User)
admin.site.register(Reservation)
admin.site.register(ReservationsChoice)
