#!/usr/bin/python
import boto3

iam_client = boto3.client('iam')
attached_user_policies = iam_client.list_attached_user_policies(
    UserName='mahesh',
)

print(attached_user_policies)

policy_details = iam_client.get_policy(
    PolicyArn = 'arn:aws:iam::aws:policy/AdministratorAccess'
)
print('policy details')
print(policy_details)

iam = boto3.resource('iam')
user_policy = iam.UserPolicy('mahesh','AdministratorAccess')

print('User policy details')
print(user_policy)