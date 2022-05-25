from django.contrib import admin

from .models import BBooks, Album, Track, Experience, Pep, Producer, Production

admin.site.register(BBooks)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Pep)
admin.site.register(Experience)
admin.site.register(Producer)
admin.site.register(Production)
