from PIL import Image
import numpy as np
from keras import models
def predictClothes(filenameImage, filenameModel, filenameWeights):
  image = Image.open(filenameImage) # buscar imagem no diretório enviado
  image = image.convert('L') #tranformar para o formato greenscaler
  image = image.resize((28,28)) #organização do shape de entrada
  image = np.array(image, ndmin=3)/255 #normalização da imagem

  json_file = open(filenameModel, 'r') #abre o arquivo
  loaded_model_json = json_file.read() # le o arquivo em json
  json_file.close() # fecha o arquivo
  model = models.model_from_json(loaded_model_json) # carrega o modelo
  model.load_weights(filenameWeights)# carrega os pesos

  result_predict = int(model.predict_classes(image)) # faz a previsão e converte para inteiro

  nome_classes = ["Camiseta", "Calça", "Suéter", "Vestido", "Casaco","Sandália","Camisa","Tênis", "Bolsa","Botas"]
  result = str(nome_classes[result_predict])
  return result

