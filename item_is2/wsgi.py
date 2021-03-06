"""
WSGI config for item_is2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os, sys
# add the hellodjango project path into the sys.path
sys.path.append('/var/www/item_is2')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/var/www/item_is2/is2venv/lib/python3.7/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'item_is2.settings')

application = get_wsgi_application()
