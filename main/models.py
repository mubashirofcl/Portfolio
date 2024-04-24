from django.db import models

# Create your models here.
class Index_work_page(models.Model):
    work_img = models.ImageField(upload_to='index_works_page')
    work_name = models.CharField(max_length=255, default='...')
    work_dis = models.CharField(max_length=255, default='...')
      
class Music(models.Model):
    music_url = models.CharField(max_length=255, default='#')
    
    
class Contact_page(models.Model):
    NAME = models.CharField(max_length=255)
    EMAIL = models.EmailField()
    SUBJECT = models.TextField(max_length=1024,)
    SUBMITED_DATE = models.DateField(auto_now=True)
    
class projectPage(models.Model):
    project_image = models.ImageField(upload_to='projectPage')
    project_preview_img = models.ImageField(upload_to='projectPage', default='...')
    project_names = models.CharField(max_length=255, default='...')
    project_diss = models.CharField(max_length=255, default='...')  
    live_preview = models.CharField(max_length=255, default='#')
    project_main_diss = models.CharField(max_length=1024, default='...')
    project_languages_urls1 = models.CharField(max_length=255, default='#')
    project_languages_urls2 = models.CharField(max_length=255, default='#')
    project_languages_urls3 = models.CharField(max_length=255, default='#')
    project_languages_urls4 = models.CharField(max_length=255, default='#')
    project_languages_urls5 = models.CharField(max_length=255, default='#')
