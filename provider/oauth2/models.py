"""
Default model implementations. Custom database or OAuth backends need to
implement these models with fields and and methods to be compatible with the
views in :attr:`provider.views`.
"""
from .abstract_models import AbstractClient
from .abstract_models import AbstractGrant
from .abstract_models import AbstractAccessToken
from .abstract_models import AbstractRefreshToken



class AccessToken(AbstractAccessToken):

    class Meta:
        app_label = 'oauth2'


class RefreshToken(AbstractRefreshToken):

    class Meta:
        app_label = 'oauth2'


class Client(AbstractClient):

    class Meta:
        app_label = 'oauth2'


class Grant(AbstractGrant):

    class Meta:
        app_label = 'oauth2'
