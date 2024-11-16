"""
WSGI config for rafatech project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import subprocess
from pathlib import Path

from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rafatech.settings')
application = get_wsgi_application()
#try:
#    from django.core.wsgi import get_wsgi_application
#    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rafatech.settings')
#    application = get_wsgi_application()
#except ModuleNotFoundError as e:
#    # Get the module name that wasn't found
#    print(str(e))
#    missing_module = str(e).split("'")[1]
#    
#    # Search for the module file
#    result = subprocess.run(['find', '/', '-name', f'{missing_module}.py'], 
#                          capture_output=True, text=True)
#    found_paths = result.stdout.strip().split('\n')
#    
#    # Get the path that was attempted
#    current_path = str(Path(__file__).parent)
#    
#    print(f"\nError: Could not find module '{missing_module}'")
#    print(f"Current path: {current_path}")
#    print("\nPossible locations found:")
#    for path in found_paths:
#        if path:  # Skip empty lines
#            print(f"- {path}")
#            
#    raise  # Re-raise the original error
