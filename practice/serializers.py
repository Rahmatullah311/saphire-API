from rest_framework.serializers import ModelSerializer
from . import models





class TopicSerializer (ModelSerializer):
  model = models.Topic
  fields = '__all__'
  
  def create (self, validatedData):
    return self.model.objects.create(**validatedData)
  
  def update(self, instance, validatedData):
    instance.title = validatedData.get('title', instance.title)
    instance.text = validatedData.get('text', instance.text)
    instance.owner = validatedData.get('user', instance.owner)
    
    instance.save()
    return instance