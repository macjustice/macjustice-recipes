from boto3.s3.transfer import S3Transfer
import boto3
import requests
# import S3Uploader

s3_resource = boto3.resource('s3')

munki_bucket = s3_resource.Bucket('munki-sandbox')

munki_bucket_contents = [x.key for x in munki_bucket.objects.all()]

if

# munki_bucket.upload_file(Filename='/Users/macj/Downloads/AutoDMG-1.9.dmg', Key='AutoDMG-1.9.dmg')


# s3 = boto3.client('s3')
# url = s3.generate_presigned_url(ClientMethod='get_object', Params={'Bucket': bucket, 'Key': 'chrome.dmg'})


# client = boto3.client('s3', 'us-west-2')
# transfer = S3Transfer(client)

# transfer.upload_file(filename="", bucket=bucket, key="")
