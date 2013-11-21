import sys
#sys.path.append('~/Dev/ovo_dev/onevone')
from django.contrib import admin
from models import Team, Player, User
# Register your models here.

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(User)
