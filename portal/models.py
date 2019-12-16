from django.db import models
from django.contrib.flatpages.models import FlatPage
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import os

class FlatPageAddon(models.Model):
    flatpage = models.OneToOneField(FlatPage, on_delete=models.CASCADE)
    header = models.TextField(blank=True)
   
    def __str__(self):
        return "%s - %s" %(str(self.id), self.flatpage.title)

class Template(models.Model):
    file_name = models.CharField(_('name'), max_length=50)
    content = models.TextField(_('content'), blank=True, null=True)
    file = models.FileField(upload_to='templates', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_saved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.file_name

class FilePage(models.Model):
    name = models.CharField(_('name'), max_length=50)
    slug = models.SlugField(_('slug'),unique=True, blank=True)
    description = models.TextField(_('description'),blank=True, null=True)
    publish = models.BooleanField(default = True)
    template_name = models.CharField(
        _('template name'),
        max_length=70,
        blank=True,
        help_text=_(
            'Example: “flatpages/contact_page.html”. If this isn’t provided, '
            'the system will use “flatpages/default.html”.'
        ),
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(FilePage, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

class UploadFile(models.Model):
    file_type = models.ForeignKey(FilePage, on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)
    upload_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    file = models.FileField(upload_to='upload_file')

    @property
    def filename(self):
        return os.path.basename(self.file.name)
    
    @property
    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension

    def __str__(self):
        return "%s - %s"%(self.id, self.file_type.name)

