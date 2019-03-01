import collections
import os
import sys

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line, text')
def print_header():
  print("----------------------------")
  print("      File Search App")
  print("----------------------------")

def get_folder_from_user():
  folder = input("What folder do you want to search? ")
  if not folder or not folder.strip():
    return None
  if not os.path.isdir(folder):
    return None
  return os.path.abspath(folder)

def get_search_text_from_user():
  text = input("What are you searching for [single phrase only]? ")
  if not text or not text.strip():
    return None
  else:
    return text

def search_files(filename, text):
  count = 0
  with open(filename, 'r', encoding='utf-8') as infile:
    for line in infile:
      count += 1
      if line.lower().find(text) >= 0:
        m = SearchResult(file=filename, line=count, text=line)
        yield m
  
def search_folders(folder, text):
  print("Searching {} for {}".format(folder, text))
  items = os.listdir(folder)
  for item in items:
    print("searching {}.....".format(item))
    full_item = os.path.join(folder, item)
    if os.path.isdir(full_item):
      yield from search_folders(full_item)
    else:
      yield from search_files(full_item, text)


def main():
  print_header()
  folder = get_folder_from_user()
  if not folder:
    print("Sorry, unable to search that location.")
    sys.exit(1)
  text = get_search_text_from_user()
  if not text:
    print("Cannot search for nothing")

  matches = search_folders(folder, text)
  for match in matches:
    print("file: {}, line no: {}, text: {}".format(match.file, match.line,
                                                match.text))

if __name__ == '__main__':
  main()
