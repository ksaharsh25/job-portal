from django.contrib import admin
from . models import Country, State, City
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    change_list_template='admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template='admin/add_form.html'

    menu_title = "Country"
    menu_group = "World"

    search_fields = ['country']
    list_display = ['id', 'country']


@admin.register(State)
class StateAdmin(ImportExportModelAdmin):
    change_list_template='admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template='admin/add_form.html'

    menu_title = "state"
    menu_group = "World"

    search_fields = ['country__country', 'state']
    list_display = ['state', 'country']

    autocomplete_fields = ['country']
    list_select_related = ['country']


# @admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    change_list_template='admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template='admin/add_form.html'


    menu_title = "City"
    menu_group = "World"


    search_fields = ['country__country','state__state', 'city',]
    list_display = ['id','state','city',]

   # autocomplete_fields = ['state','country']
    list_select_related = ['state']

admin.site.register(City,CityAdmin)
