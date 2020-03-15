#!/usr/bin/python
import boto3

iam_client = boto3.client('iam')

# This script would get
# 1. User list(s)
# 2. Group Details
# 3. Policy details

# Dictionary to get all iam users
user_details={}
iam_account_details = iam_client.get_account_authorization_details()

print(iam_account_details)

# Create through the list and add specified details in dictionary format
for user in iam_account_details['UserDetailList']:
    username = user['UserName']
    policies = user['AttachedManagedPolicies']

    user_details[username] = {
            'userId': user['UserId'],
            'arn': user['Arn'],
            'groups': user['GroupList'],
            'policies': policies,
            'createDate': user['CreateDate'],
        }

for key in user_details:
    print(key)
    print('User ID: ',     user_details[key]['userId'])
    print('arn: ',         user_details[key]['arn'])
    print('groups: ',      user_details[key]['groups'])
    print('policies: ',    user_details[key]['policies'])
    print('Create Date: ', user_details[key]['createDate'])
    print("\n")
