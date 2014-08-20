from django.contrib import admin
from django.db.models import get_model


Client = get_model('oauth2', 'Client')
Grant = get_model('oauth2', 'Grant')
RefreshToken = get_model('oauth2', 'RefreshToken')
AccessToken = get_model('oauth2', 'AccessToken')


class AccessTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'token', 'expires', 'scope',)
    raw_id_fields = ('user',)


class GrantAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'code', 'expires',)
    raw_id_fields = ('user',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('url', 'user', 'redirect_uri', 'client_id', 'client_type')
    raw_id_fields = ('user',)

admin.site.register(AccessToken, AccessTokenAdmin)
admin.site.register(Grant, GrantAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(RefreshToken)
