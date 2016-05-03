# -*- coding: utf-8 -*-
# 管理サイト表示オブジェクト

from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# モデルChoice用管理オブジェクト
#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    # モデル：Choice
    model = Choice
    # 個数：3つ
    extra = 3

# モデルQuestion用管理オブジェクト
class QuestionAdmin(admin.ModelAdmin):
    # 入力フィールド（日付（pub_date）、質問文（questio_text））
    # fields = ['pub_date', 'question_text']

    # 辞書として入力項目を定義
    # ①タイトル：なし(None)で入力項目：Questionのquestion_text
    # ②タイトル：Date informationで入力項目：Questionのpub_date
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # Choice（3つ）の編集項目
    inlines = [ChoiceInline]

    # 一覧画面では3つの項目を表示
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # チェンジリストページにフィルタサイドバー（日付：pub_date）を追加
    list_filter = ['pub_date']

    #  チェンジリストページに検索機能を追加
    search_fields = ['question_text']

# 管理サイトにQuestionを登録、画面はQuestionAdminに従う
admin.site.register(Question, QuestionAdmin)
# 管理サイトにChoiceを登録
admin.site.register(Choice)
