from google.cloud import datastore, storage
import time

datastore_client = datastore.Client()
storage_client = storage.Client()

def get_list_of_files(bucket_name):
    """Lists all the blobs in the bucket."""
    print("\n")
    print("get_list_of_files: "+bucket_name)

    blobs = storage_client.list_blobs(bucket_name)
    print(blobs)
    files = []
    for blob in blobs:
        if blob.name.lower().endswith(('.jpeg', '.jpg')):
            files.append(blob.name)

    return files

def upload_file(bucket_name, source_path, file_name):
    """Send file to bucket."""
    print("\n")
    print("upload_file: "+bucket_name+"/"+file_name)

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    blob.upload_from_filename(source_path)

def download_file(bucket_name, file_name):
    """ Retrieve an object from a bucket and saves locally"""  
    print("\n")
    print("download_file: "+bucket_name+"/"+file_name)
    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(file_name)
    blob.download_to_filename(file_name)
    blob.reload()
    return
