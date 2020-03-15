#!/usr/bin/python
import boto3

ec2_client = boto3.client('ec2')

# Retrieves all regions/endpoints that work with EC2
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

print(regions)

# Retrieves availability zones only for region of the ec2 object
# Passing regions won't help in this way
azs = [az['ZoneName'] for az in ec2_client.describe_availability_zones(Filters=[
        {
            'Name': 'region-name',
            'Values': regions
        }
    ])['AvailabilityZones']]
print(azs)

# Retrieves all regions/endpoints that work with EC2
aws_regions = ec2_client.describe_regions()

# Get a list of regions and then instantiate a new ec2 client for each region in order to get list of AZs for the region
for region in aws_regions['Regions']:
    current_region_name = region['RegionName']
    ec2_region = boto3.client('ec2', region_name=current_region_name)
    region_filter = [{'Name': 'region-name', 'Values': [current_region_name]}]
    print ("Current Region is %s" % current_region_name)
    aws_azs = ec2_region.describe_availability_zones(Filters=region_filter)
    for az in aws_azs['AvailabilityZones']:
        zone = az['ZoneName']
        print(zone)