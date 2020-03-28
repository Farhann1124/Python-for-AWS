#!/usr/bin/python
import boto3

ec2_client = boto3.client('ec2')

# Retrieves all regions/endpoints that work with EC2
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

for region in regions:
    print("Config rule check in Region: ", region)

    config_client = boto3.client('config', region_name=region)
    config_details = config_client.describe_compliance_by_resource()
    print(config_details)

    trail_client = boto3.client('cloudtrail', region_name=region)
    trails = trail_client.describe_trails()
    print(trails)




