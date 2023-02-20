from django.contrib import admin
from . models import Member
from guardian.admin import GuardedModelAdmin



class AuthorAdmin(GuardedModelAdmin):
    pass

admin.site.register(Member,AuthorAdmin)