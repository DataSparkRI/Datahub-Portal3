from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from portal.models import FilePage, UploadFile
from django.conf import settings
from django.template.defaultfilters import filesizeformat

def filepage(request, slug):
    f = get_object_or_404(FilePage, slug=slug, publish=True)
    files = UploadFile.objects.filter(file_type = f).order_by('-upload_at')
    if f.template_name:
       template_name = f.template_name
    else:
       template_name = 'flatpages/default.html'
    content = """
		<table class="table">
		  <thead class="thead-light">
		    <tr>
		      <th scope="col">File Name</th>
		      <th scope="col">Type</th>
		      <th scope="col">Size</th>
		      <th scope="col">Date Upload</th>
		      <th scope="col">Download</th>
		    </tr>
		  </thead>
		  <tbody>"""
    for i in files:
        content = content + """
		    <tr>
		      <th scope="row">%s</th>
		      <td>%s</td>
		      <td>%s</td>
		      <td>%s</td>
                      <td><a href="%s">Download</a></td>
		    </tr>"""%(i.filename, i.extension, filesizeformat(i.file.size), i.upload_at.strftime('%Y-%m-%d %H:%M'), i.file.url)
    content = content + "</table>"
    filepage = {
                 "title": f.name,
                 "content": content,
                 "header": f.description,
               }

    return render(request, template_name, filepage)

