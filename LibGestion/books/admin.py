from django.contrib import admin
from books.models import User,book,book_fav,FeedBack
# Register your models here.
admin.site.register(User)
admin.site.register(book)
admin.site.register(book_fav)
admin.site.register(FeedBack)
