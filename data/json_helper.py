import os
import json
import pickle

def read_json(file_path: str) -> object: ##part A
   with open(file_path, 'r') as file:
      json_data= json.load(file)
      return json_data

def read_all_json_files(directory_path: str): #part B
   json_data = []
   #  for root, _, files in os.walk(directory_path):
   for filename in os.listdir(directory_path):
      if filename.endswith('.json'):
         filepath = os.path.join(directory_path, filename)
         json_data.append(read_json(filepath))
   return json_data
      
def write_pickle(file_path, data): #part C
      pickle_file = os.path.join(file_path, 'super_smash_characters.pickle')
      with open(pickle_file, 'wb') as file:
         pickle.dump(data, file)

def load_pickle(file_path): #part D
      with open(file_path, 'rb') as file:
         data = pickle.load(file)
         return data