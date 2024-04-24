from django.contrib import admin
from .models import Index_work_page, Music, Contact_page, projectPage
# Register your models here.

class index_WorkAdmin(admin.ModelAdmin):
    list_display = ('work_name', 'work_img','work_dis')
admin.site.register(Index_work_page, index_WorkAdmin)


class MusicAdmin(admin.ModelAdmin):
    list_display = ('id','music_url')
admin.site.register(Music, MusicAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','NAME','EMAIL','SUBJECT', 'SUBMITED_DATE')
admin.site.register(Contact_page, ContactAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_image','project_preview_img', 'project_names','project_diss', 'live_preview', 'project_main_diss', 'project_languages_urls1', 'project_languages_urls2', 'project_languages_urls3', 'project_languages_urls4', 'project_languages_urls5', 'id')
admin.site.register(projectPage, ProjectAdmin)