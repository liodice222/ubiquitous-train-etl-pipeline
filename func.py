import oci

config = oci.config.from_file('config.ini')

object_storage_client = oci.object_storage.ObjectStorageClient(config)
namespace = object_storage_client.get_namespace().data

bucket_name = "DEP-ASH-OBJ-01"

try:
    objects = object_storage_client.list_objects(namespace, bucket_name)
    for obj in objects.data.objects:
        print(obj.name)
except oci.exceptions.ServiceError as e:
    print(f"Service error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")