from django.contrib import admin

from .models import Question, Poll


class QuestionAdmin(admin.ModelAdmin):
    pass


class PollAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)
admin.site.register(Poll, PollAdmin)
