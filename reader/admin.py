from django.contrib import admin
from .models import MajorArcanaCard
from .models import MinorArcanaCard
from .models import Spread
from .models import Placement

# Register models
admin.site.register(MajorArcanaCard)
admin.site.register(MinorArcanaCard)
admin.site.register(Spread)
admin.site.register(Placement)
