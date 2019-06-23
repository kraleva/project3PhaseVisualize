from django.contrib import admin

from .models import User
from .models import Following
from .models import Tweet
from .models import Relationship

admin.site.register(Following)
admin.site.register(Relationship)
admin.site.register(Tweet)
admin.site.register(User)
