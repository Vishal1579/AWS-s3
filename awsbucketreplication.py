import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    source_bucket_name = 'awsbuck1'
    destination_bucket_name = 'awsbuck2'

    source_bucket = s3.Bucket(source_bucket_name)
    destination_bucket = s3.Bucket(destination_bucket_name)

    for obj in source_bucket.objects.all():
        source_key = obj.key
        print(f'Copying file {source_key} to destination bucket...')
        # Copy the object from the source bucket to the destination bucket
        destination_bucket.copy({'Bucket': source_bucket_name, 'Key': source_key}, source_key)

    print('All files copied from source bucket to destination bucket.')
