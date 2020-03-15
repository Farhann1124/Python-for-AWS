#!/usr/bin/python
import boto3

# Get all security groups used by instances
ec2 = boto3.client('ec2')

security_groups_in_use = []
public_ec2_count = 0
ec2_instance_sg_count = 0

instances_dict = ec2.describe_instances()
reservations = instances_dict['Reservations']
for i in reservations:
    for j in i['Instances']:
        for k in j['SecurityGroups']:
            if k['GroupId'] not in security_groups_in_use:
                security_groups_in_use.append(k['GroupId'])
                try:
                    if j['PublicIpAddress']:
                        public_ec2_count +=1
                except KeyError:
                    pass
                ec2_instance_sg_count += 1
print(ec2_instance_sg_count)
print(security_groups_in_use)