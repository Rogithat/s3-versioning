#!/usr/bin/env python

'''
Maintainer: Igor Santos Ferreira
Function: DevSecOps Engineer
Description: In order to avoid losing data in our S3 buckets, it's necessary to apply lifecycle policies with coherent retention period and bucket versioning 
to ensure that all data is there when we need it
'''

import boto3
import emoji

s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')

def get_bucket_status(bucket_name):
    
    versionEnabled = s3.get_bucket_versioning(Bucket = bucket_name)
    return versionEnabled['Status']

def set_bucket_versioning(bucket_name):
    versioning = s3_resource.BucketVersioning(bucket_name)
    versioning.enable()



def main():
    bucketList = s3.list_buckets()

    for each_bucket in bucketList['Buckets']:

        try:
            get_bucket_status(each_bucket['Name']) == "Enabled"
            print("Versioning is already enabled on", each_bucket['Name'], "OK!")
        except:
            print("Versioning not enabled on bucket",each_bucket['Name'], "NOK!")
            print("Enabling versioning to match AWS Backup requisites")
            set_bucket_versioning(each_bucket["Name"])


main()
    


