from django.contrib import admin
from .models import Plot, Comment, Reply, LikedPlot, LikedComment

admin.site.register(Plot)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(LikedPlot)
admin.site.register(LikedComment)