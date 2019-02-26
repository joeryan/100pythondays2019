import os
import requests
import shutil

def get_data_from_url(url):
  data = requests.get(url, stream=True)
  return data.raw

def get_cat(folder, name):
  url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
  print("getting {} ....".format(name))
  data = get_data_from_url(url)
  print("Saving {} to {} ....".format(name, folder))
  file_name = os.path.join(folder, name + ".jpg")
  with open(file_name, 'wb') as fout:
    shutil.copyfileobj(data, fout) 


