from django.contrib import admin
from .models import ACTIVITY
from .models import PEOPLE
from .models import CALCULATION

admin.site.register(ACTIVITY)
admin.site.register(PEOPLE)
admin.site.register(CALCULATION)

