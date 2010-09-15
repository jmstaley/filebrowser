import os
from django.conf import settings
from django.shortcuts import render_to_response

FILE_EXTENTIONS = ('jpg', 'gif', 'png')

def browse(request):
    files_info = []
    path = os.path.join(settings.MEDIA_ROOT, settings.IMAGEBROWSER_DIR)
    if os.path.isdir(path):
        files = os.listdir(path)

        for file_name in files:
            name, ext = file_name.split('.')
            if ext in FILE_EXTENTIONS:
                files_info.append((os.path.join('/', 
                                                settings.IMAGEBROWSER_DIR, 
                                                file_name), 
                                   file_name))

    return render_to_response('imagebrowser/index.html', 
                              {'files': files_info,
                               'title': 'Image Browser'})
