from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from portal.models import FilePage, UploadFile, Template
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from django.contrib.admin.views.decorators import staff_member_required
from portal.forms import TemplateForm

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
        try:
           content = content + """
		    <tr>
		      <th scope="row">%s</th>
		      <td>%s</td>
		      <td>%s</td>
		      <td>%s</td>
                      <td><a href="%s">Download</a></td>
		    </tr>"""%(i.filename, i.extension, filesizeformat(i.file.size), i.upload_at.strftime('%Y-%m-%d %H:%M'), i.file.url)
        except:
           content = content + """
		    <tr>
		      <th scope="row">%s</th>
		      <td>%s</td>
		      <td>%s</td>
		      <td>%s</td>
                      <td><a href="%s">Download</a></td>
		    </tr>"""%('N/A', "N/A", "N/A", i.upload_at.strftime('%Y-%m-%d %H:%M'), i.file.url)
    content = content + "</table>"
    filepage = {
                 "title": f.name,
                 "content": content,
                 "header": f.description,
               }

    return render(request, template_name, filepage)

@staff_member_required(login_url='/accounts/login/')
def edit_template(request, template_id):
    template = get_object_or_404(Template, id=template_id)
    if request.method == "POST":
        form = TemplateForm(request.POST or None, instance=template)
        if form.is_valid():
            template = form.save(commit=False)
            template.save()
            return JsonResponse({"message":"Saved"}, safe=False)
    else:
        form = TemplateForm(request.POST or None, instance=template)

    context = {'form': form,
               'template':template}
    return render(request, 'template/editor.html', context)


    

