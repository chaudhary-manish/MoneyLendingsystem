# MoneyLendingsystem
to connect mysql with django in p3
1: apt-get install python-mysqldb
2: pip install mysql-connector-python --allow-external mysql-connector-python 
3: DATABASES = {
    'default': {
        'NAME': 'user_data',
        'ENGINE': 'mysql.connector.django',
        'USER': 'mysql_user',
        'PASSWORD': 'priv4te',
        'OPTIONS': {
          'autocommit': True,
        },
    }
}

to create migration we have to update setting file
'moneymanagement.apps.MoneymanagementConfig',

MoneymanagementConfig imp


