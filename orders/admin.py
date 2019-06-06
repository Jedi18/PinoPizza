from django.contrib import admin

from .models import PizzaAndSubs, Others, ToppingsAndExtra
# Register your models here.
admin.site.register(PizzaAndSubs)
admin.site.register(Others)
admin.site.register(ToppingsAndExtra)
