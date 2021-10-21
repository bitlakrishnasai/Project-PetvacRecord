from django.contrib import admin
from vacRecords.models import User,Pet,Health,Vaccine,Medicines,Checkup

admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Health)
admin.site.register(Vaccine)
admin.site.register(Medicines)
admin.site.register(Checkup)

# Register your models here.
