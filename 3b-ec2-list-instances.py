#!/usr/bin/python
import boto3
ec2client = boto3.client('ec2')
instances = ec2client.describe_instances()

for reservation in instances["Reservations"]:
    for instance in reservation["Instances"]:
        # This will print will output the value of the Dictionary key 'InstanceId'
        print("Instance ID: ", instance["InstanceId"])
        print("Image ID: ", instance["ImageId"])
        print("Instance Type: ", instance["InstanceType"])
        print("public ip: ",instance["PublicIpAddress"])
        print("private ip: ",instance["PrivateIpAddress"])
        print("AZ: ", instance["Placement"]["AvailabilityZone"])
    print("\n")