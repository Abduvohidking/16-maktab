from django.contrib import admin

# Register your models here.
from myapp.models import kitob, audio_kitob, audio

admin.site.register(kitob)
admin.site.register(audio_kitob)
admin.site.register(audio)