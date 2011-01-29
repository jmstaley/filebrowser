import os
from django.conf import settings
from django.shortcuts import render_to_response
from django.db.models import get_model

def browse(request, file_type):
    image_model, appname = settings.BROWSER_IMAGE
    file_model, appname = settings.BROWSER_FILE
    files_info = []

    if file_type == 'image':
        model_name, appname = settings.BROWSER_IMAGE
        fieldname = 'image'
    elif file_type == 'file':
        model_name, appname = settings.BROWSER_FILE
        fieldname = 'document'

    model = get_model(appname, model_name)

    objs = model.objects.all()
    for obj in objs:
        field = getattr(obj, fieldname)
        files_info.append((field.name, 
                           obj.title))

    return render_to_response('filebrowser/index.html', 
                              {'files': files_info,
                               'type': file_type,
                               'title': '%s Browser' % file_type.capitalize()})
