from django.contrib import admin
from .models import MajorArcanaCard
from .models import MinorArcanaCard

# Register models
admin.site.register(MajorArcanaCard)
admin.site.register(MinorArcanaCard)
