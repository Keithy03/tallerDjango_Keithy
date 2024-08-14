from django.contrib import admin

from .models import Question, Choice


# Al momento de crear una question se podran agregar o editar existentes al mismo tiempo las chice.
# Une ambos formularios.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

# Nota es muy util cuando hay muchos campos.
class QuestionAdmin(admin.ModelAdmin):
    # Para acomodar los campos que uno desee primero.
    # fields = ["pub_date", "question_text"]

    # Para acomodar los campos en el orden que uno desee y en diferentes bloques o grupos.
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    # Para que una ambos formularios
    inlines = [ChoiceInline]
    # Muestra informacion de la publicación o creación de las Questions
    list_display = ["question_text", "pub_date", "was_published_recently"]
    # Agrega un cuadro de filtros.
    list_filter = ["pub_date"]
    # Agrega un cuadro de busqueda.
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)
