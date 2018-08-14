# all_users admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from all_users.models import User

# Add an extra field to the UserAdmin page. Since the User model has a set
# field set, we need to append my custom field on top of the fields.

fsets = list(UserAdmin.fieldsets)
fsets.append((_('Custom Fields'), {'fields': ('user_type',)}))
fsets = tuple(fsets)

class AllUserAdmin(UserAdmin):

    fieldsets = fsets

admin.site.register(User, AllUserAdmin)