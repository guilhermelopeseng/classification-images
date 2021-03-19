import uuid
from django.db import models
from stdimage.models import StdImageField

from django.db.models import signals

import clothesClassification
from clothesClassification.settings import BASE_DIR

import src
from src.classification.predict import predictClothes

def get_file_path(instace, filename):
  ext = filename.split('.')[-1]
  filename = f'{uuid.uuid4()}.{ext}'
  return filename

class Image(models.Model):
  image = StdImageField('Imagem', upload_to=get_file_path, delete_orphans=True)
  predict = models.CharField('Previsão', null=True, blank=True, max_length=15)
  
  created_at = models.DateField('Criado em', auto_now_add=True)
  updated_at = models.DateField('Atualizado em', auto_now=True)
  is_activated = models.BooleanField('Está Ativo', default=True)

  class Meta:
    verbose_name = 'Imagem'
    verbose_name_plural = 'Imagens'
  
  def __str__(self):
    return f'{self.predict}: {self.image}'

def image_post_save(signal, instance, sender, **kwargs):
  signals.post_save.disconnect(image_post_save, sender=Image)
  filenameImage = BASE_DIR/'media'/instance.image.name
  filenameModel = BASE_DIR/'models'
  instance.predict = predictClothes(filenameImage,filenameModel)
  instance.save()
  signals.post_save.connect(image_post_save, sender=Image)

signals.post_save.connect(image_post_save, sender=Image)



