from rest_framework import serializers
from .models import course

class courseserializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=course
		fields=('id','url','name','language','price')

