from django.contrib import admin
from .models import Topic, Webpage, AccessRecords, User

# Register your models here.

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecords)
admin.site.register(User)
