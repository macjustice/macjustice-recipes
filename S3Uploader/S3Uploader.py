#!/usr/bin/env python

#
# Copyright 2019 MacGregor Justice
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import boto3
from autopkglib import Processor, ProcessorError


# __all__ here means that all symbols of the S3Uploader class will be imported if something calls "from S3Uploader import *"
__all__ = ["S3Uploader"]


class S3Uploader(Processor):

    """Processor base class.

      Processors accept a property list as input, process its contents, and
      returns a new or updated property list that can be processed further.
      """

    description = __doc__
    input_variables = {
        "pkg_path": {
            "required": True,
            "description": "Path to a pkg or dmg to upload."
        },
        "bucket_name": {
            "required": True,
            "description": "Name of the S3 bucket to upload to."
        },
    }

    output_variables = {
        "s3_path": {
            "description": "Outputs path to pkg from bucket root"
        },
        "s3_url": {
            "description": "Outputs URL of uploaded pkg"
        }
    }

    def main(self):

        package = self.env["pkg_path"]

        print(package)

        # Check if Boto3 installed
        try:
            import boto3
        except(ImportError):
            print('This plugin uses the boto3 module. Please install it with:\n'
                  '   pip install boto3 --user')
            exit(1)

        # Check ~/.aws config or profile domain??
        try:
            s3_resource = boto3.resource('s3')
            munki_bucket = s3_resource.Bucket('munki-sandbox')
        except(NoCredentialsError):
            print('The boto3 module requires AWS credentials. See this doc for more info:\n'
                  '   https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html')
            exit(1)

        # See if pkg is already in S3, then upload
        munki_bucket_contents = [x.key for x in munki_bucket.objects.all()]
        if package not in munki_bucket_contents:
            munki_bucket.upload_file(Filename=package, Key='AutoDMG-1.9.dmg')
        else:
            raise Exception(
                'A file with the same name already exists in this bucket.')
        # Return output variables


if __name__ == "__main__":
    PROCESSOR = S3Uploader()
    PROCESSOR.execute_shell()
