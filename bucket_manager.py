#!/usr/bin/env python

'''
Maintainer: Igor Santos Ferreira
Function: DevSecOps Engineer
Description: Simple script developed in order to avoid losing data in S3 buckets, it's necessary to enblae versioning on bucket to match an AWS Backup requisite as described
in: https://docs.aws.amazon.com/pt_br/aws-backup/latest/devguide/s3-backups.html
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
            print("Versioning is already enabled on", each_bucket['Name'], emoji.emojize(':check_mark:'))
        except:
            print("Versioning not enabled on bucket",each_bucket['Name'], emoji.emojize(':cross_mark:'))
            print("Enabling versioning to match AWS Backup requisites")
            set_bucket_versioning(each_bucket["Name"])


main()
    


