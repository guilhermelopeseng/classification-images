from PIL import Image, ImageOps
import numpy as np
from tensorflow.keras import models
from tensorflow.keras.datasets import fashion_mnist


def predictClothes(filenameImage, filenameModel):
  image = Image.open(filenameImage) # buscar imagem no diretório enviado
  image = image.resize((28,28)) #organização do shape de entrada
  image = ImageOps.grayscale(image) #tranformar para o formato grayscaler
  image = np.array(image, ndmin=3)/255 #normalização da imagem

  model = models.load_model(filenameModel)

  result_predict = int(np.argmax(model.predict(image),axis=-1)) #faz a previsão
  print(np.argmax(model.predict(image),axis=-1))
  print(model.predict(image))

  nome_classes = ["Camiseta", "Calça", "Suéter", "Vestido", "Casaco","Sandália","Camisa","Tênis", "Bolsa","Botas"]
  result = str(nome_classes[result_predict])
  return result

