from django.contrib import admin
from blog import models
from .models import Post 
from .models import Category


# Register your models here.






class catAdmin(admin.ModelAdmin):

    list_display = ("name", "status","id")
    
admin.site.register(Category , catAdmin)





class postAdmin(admin.ModelAdmin):

    list_display = ("user", "title" ,"slug","id","category",)
    

admin.site.register(Post , postAdmin)