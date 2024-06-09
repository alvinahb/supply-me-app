from django.contrib import admin

from supplyme.models import (Category,
                             Organization,
                             Product,
                             User)


admin.site.register(Category)
admin.site.register(Organization)
admin.site.register(Product)
admin.site.register(User)
