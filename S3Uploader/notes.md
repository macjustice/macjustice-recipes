
[https://realpython.com/python-boto3-aws-s3/#python-code-or-infrastructure-as-code-iac](https://realpython.com/python-boto3-aws-s3/#python-code-or-infrastructure-as-code-iac) 

## For comparison
https://github.com/autopkg/homebysix-recipes/tree/master/VersionSplitter
https://github.com/autopkg/recipes/tree/master/SampleSharedProcessor



1. Read AWS credentials, 
2. Upload file to S3 bucket
3. Return URL/path?


```python
from boto.s3.transfer import S3Transfer
import boto3

client = boto3.client('s3', 'us-west-2')
transfer = S3Transfer(client)

transfer.upload_file(filename='path/to/file', bucket='bucket_name', key='filename_in_bucket')
```

