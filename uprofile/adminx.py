import xadmin
from .models import Uprofile

class UserProfileXadmin(object):
    list_display = ('username', 'nick_name', 'ucellphone', 'uposition',)
    model_icon = 'fa fa-user'

xadmin.site.unregister(Uprofile)
xadmin.site.register(Uprofile, UserProfileXadmin)