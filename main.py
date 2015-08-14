# -*- coding: utf-8 -*-

# Un poco de hackeo para tener los módulos necesarios.

import os
import sys

os.environ["DJANGO_SETTINGS_MODULE"] = 'foe_gae.settings'

sys.path.append(
    os.path.dirname(
        os.path.abspath(__file__)
    ) + '/libs'
)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
