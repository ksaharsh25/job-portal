from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

# from address.models import Address
# from address.forms import AddressForm
from tabbed_admin import TabbedModelAdmin

User = get_user_model()

# class AddressInline(admin.StackedInline):
#     model = Address
#     extra = 0

#     form = AddressForm
#     pass


@admin.register(User)
class UserAdmin(BaseUserAdmin, TabbedModelAdmin):

    change_list_template = 'admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template = 'admin/add_form.html'

    menu_title = "User"
    menu_group = "Auth"

    tab_general_information = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': [
            'mobile_number',
            'alternate_number',
            'user_type',
           
            'first_name',
            'middle_name',
            'last_name',
            'date_of_birth',
            'gender'
        ]}),
    )
    tab_permissions = (
        ('Permissions', {'fields': [
         'staff', 'active', 'groups', 'user_permissions']}),
    )
    tabs = [
        ('General Information', tab_general_information),
        ('Permissions', tab_permissions),
    ]

   
    form = UserAdminChangeForm  # edit view
    add_form = UserAdminCreationForm  # new user form

    _group = [ 'first_name',
              'middle_name', 'last_name', 'email']
    list_filter = ['user_type', 'active', 'staff']
    list_display = ['user_id', 'full_name', 'email',
                    'user_type', 'mobile_number', 'active', 'staff']
    
    search_fields = ['user_id', 'first_name', 'email',
                    'user_type', 'mobile_number',]

    ordering = ['user_id', ]
    filter_horizontal = ['groups', 'user_permissions']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': [
            'mobile_number',
            'alternate_number',
            'user_type',
         
            'first_name',
            'middle_name',
            'last_name',
            'date_of_birth',
            'gender'
        ]}),
        ('Permissions', {'fields': [
         'staff', 'active', 'groups', 'user_permissions']}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ['wide', ],
            'fields': ['email', 'password1', 'password2', 'user_type', 'mobile_number', 'staff', 'active', 'groups', 'user_permissions']}
         ),
    )



