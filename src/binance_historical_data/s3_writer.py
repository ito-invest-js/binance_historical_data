import boto3 
import zipfile 
from datetime import * 
from io import BytesIO 
import json 
import re 
import tempfile
import urllib.request

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

class S3DataWriter():

  def __init__(
            self,
            path_dir_where_to_dump
    ) -> None:
    self.s3 = boto3.client('s3')
    self.bucket_name, self.path_key = path_dir_where_to_dump[5:].split('/', 1)

  def create_dir(self,str_dir_where_to_save):
    bucket_name, path_key = str_dir_where_to_save[5:].split('/', 1)
    self.s3.put_object(Bucket=bucket_name, Key=(path_key+'/'))
    
  def delete(self, path_to_delete):
    bucket_name, path_key = path_to_delete[5:].split('/', 1)
    self.s3.delete_object(Bucket=bucket_name, Key=path_key)
    
  def urlretrieve(self, str_url_path_to_file, str_path_where_to_save):
    bucket_name, path_key = str_path_where_to_save[5:].split('/', 1)
    with tempfile.NamedTemporaryFile(suffix='.zip') as t:
        urllib.request.urlretrieve(str_url_path_to_file, t.name)
        self.s3.upload_file(t.name, bucket_name, path_key)