# lol cat factory app
# download cat images into a subfolder in home
# launch sub-process to view images 

import cat_downloader
import os
import platform
import subprocess
import sys

def print_header():
  print("---------------------------------")
  print("\tlol cat factory")
  print("---------------------------------")

def create_output_folder():
  base_path = os.path.dirname(os.path.abspath(__file__))
  folder = 'cat_pictures'
  full_path = os.path.join(base_path, folder)
  if os.path.exists(full_path) and os.path.isdir(full_path):
    print("Cat picture directory already exists.")
  else:
    print("creating new cat picture dircetory....")
    os.mkdir(full_path)
  return full_path

def download_cat_images(folder):
  cat_count = input("How many lolcats do you want? ")
  try:
    cat_count = int(cat_count)
  except ValueError as err:
    print("You must enter an integer count of lolcats.")
    print("\t>^.^<\n\t  -") 
    sys.exit(100)
  for i in range(1, cat_count+1):
    name = "lolcat_{}".format(i)
    cat_downloader.get_cat(folder, name)

def open_cat_images(folder):
  if platform.system() == 'Linux':
    subprocess.call(['xdg-open',folder])
  elif platform.system() == 'Darwin':
    subprocess.call(['open', folder])
  else:
    subprocess.call(['explorer', folder])

def main():
  print_header()
  cat_folder = create_output_folder()
  download_cat_images(cat_folder)
  open_cat_images(cat_folder)
  print("yay, cats")

if __name__ == '__main__':
  main()
