from django.db import models


class Articles(models.Model):
    title = models.CharField('Title', max_length=550)
    abstract = models.TextField('Abstract')
    owner = models.CharField('Owner', max_length=250)
    date = models.DateTimeField('Published')
    keywords = models.CharField('Keywords', max_length=550)
    job = models.CharField("Owner's job", max_length=550)
    file_name = models.CharField("File name", max_length=550)
    
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class UploadFile(models.Model):
    title = models.CharField(max_length=250, default='')
    file = models.FileField(upload_to='')
    
    
    
    
