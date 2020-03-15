#!/usr/bin/python
import boto3
iam_client = boto3.client('iam')

# This script would do below tasks
# 1. Create User
# 2. Edit user
# 3. Delete user

'''
# 1. Create user
print("Creating a user")
try:
    create_user = iam_client.create_user(
        UserName='Mahesh-Bheema'
    )
    print("Created a user. Below is the result")
    print(create_user)
except Exception as e:
    print(e)
    pass


# 2. Edit/Update a user
print('Updating user name')
update_user = iam_client.update_user(
    UserName='Mahesh-Bheema',
    NewUserName='Jai-Mahesh-Anna'
)
print('username updated')
print(update_user)

'''
# 3. Delete a user
print('Deleting user')
delete_user = iam_client.delete_user(
    UserName='Jai-Mahesh-Anna'
)
print('user deleted')
print(delete_user)
print('Exiting the program')

