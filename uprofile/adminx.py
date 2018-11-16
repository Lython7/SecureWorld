import xadmin
from .models import Uprofile

class UserProfileAdmin(object):
    list_display = ('username', 'nick_name', 'ucellphone', 'uposition',)

xadmin.site.unregister(Uprofile)
xadmin.site.register(Uprofile, UserProfileAdmin)