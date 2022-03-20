from config.wsgi import *
from core.erp.models import Type
# Create your tests here.


query =  Type.objects.all()
print(query)
t = Type(name="Julio")
t.save()

