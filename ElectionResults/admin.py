from django.contrib import admin

from .models import *

app_models = [
    State,
    Ward,
    Lga,
    PollingUnit,
    Party,
    Agentname,
    AnnouncedLgaResult,
    AnnouncedPuResult,
    AnnouncedStateResult,
    AnnouncedWardResult,
]

for model in app_models:    
    admin.site.register(model)
