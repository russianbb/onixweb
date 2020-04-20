import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class LocalSettings:
    """Store local setting, hidding critical information from Github"""
        
    def __init__(self):
        """initialize the local settings"""
        
        #Set ambient: 'dev' or 'prod'
        self.ambient = 'dev'
        
        #Initialize all the variables
        self.AllowedHosts = []
        self.Databases = {}
        self.Debug = ''
        self.SecretKey = ''
        
        
        #Settings for 'production' ambient
        if self.ambient == 'prod':
            self.AllowedHosts = ['127.0.0.1', 'localhost', '192.34.63.130', 'onixse.com', 'web.onixse.com']
            self.Databases = {
                'default': {
                    'ENGINE': 'django.db.backends.postgresql_psycopg2',
                    'NAME': 'onixwebdb',
                    'USER': 'admin',
                    'PASSWORD': 'sol&OX16',
                    'HOST': 'localhost',
                    'PORT': '' 
                    }
            }
            self.Debug = False
            self.SecretKey = '_9&o9o+p4yim8a@*v#w$e(gzv$qh=&sq2rh%2sttcj8(d(w_&n'
        
            
        #Settings for 'development' ambient
        if self.ambient == 'dev':
            self.AllowedHosts = ['127.0.0.1', 'localhost']
            self.Databases = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(BASE_DIR, 'development.sqlite3'),
                }
            }
            self.Debug = True
            self.SecretKey = '_9&o9o+p4yim8a@*v#w$e(gzv$qh=&sq2rh%2sttcj8(d(w_&n'