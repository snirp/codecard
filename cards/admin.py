from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin, OrderedTabularInline, OrderedInlineModelAdminMixin

from .models import Card, Stack, Question, Choice, StackCard

class StackCardInline(OrderedTabularInline):
    model = StackCard
    fields = ('stack', 'card', 'move_up_down_links',)
    readonly_fields = ('order', 'move_up_down_links',)
    extra = 1
    ordering = ('order',)


class StackAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    inlines = (StackCardInline, )


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class CardAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Card, CardAdmin)
admin.site.register(Stack, StackAdmin)
admin.site.register(Question, QuestionAdmin)
