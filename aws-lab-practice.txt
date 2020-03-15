Python Lab Practice
0. Structure: Dictionary for employees
Structure:
{ 'Employee ID':
	{ 	Name: ''
		Joined: 'yyyy-mm-dd'
		Skills: []
		Project: {}
	}
}

1. use input function to get those details form user
2. use basic regular expression for name and id validation
4. Use try except block for error handling
5. do some basic validation on those inputs

Optional
2. Define a function to pass Employeed details (input) and create a dictionary
3. Function to list employee details: pass employee ID as an argument
6. pass emp id and specific info that you want to print
7. Function to add/update/delete employee details

AWS Lab Practice (CLI and Boto3)
0. Setup AWS CLI and run `aws s3 ls`

1. Print all regions
1.1 `aws ec2 describe-regions`
1.2 `aws ec2 describe-regions --query "Regions[].{Name:RegionName}" --output text`

2. List EC2 running instances region wise
2.1 `aws ec2 describe-instances`
2.2 `aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId]' --filters Name=instance-state-name,Values=running --output text	`
2.3 loop through the regions 2.2

3.1 Print Security group name attached with each ec2 instances using filters
3.2 Print security group name with ingress rules attached with each ec2 instances

4.1 List all s3 buckets: `aws s3 ls`
4.2 List only public s3 buckets: `aws s3api get-bucket-policy --bucket video-dlwd` can help
4.3 download bucket files: `aws s3 sync s3://video-dlwd .`
4.4 Get bucket policy: `aws s3api get-bucket-policy --bucket video-dlwd --query Policy --output text > policy.json`
4.5 Get bucket location: `aws s3api get-bucket-location --bucket video-dlwd`

5. Get IAM user details: `aws iam list-users`


##### BONUS #####
Example of click

import click
def greeter(**kwargs):
    output = '{0}, {1}!'.format(kwargs['greeting'],
                                kwargs['name'])
    if kwargs['caps']:
        output = output.upper()
    print(output)

@click.group()
def greet():
    pass

@greet.command()
@click.argument('name')
# add an option with 'Hello' as the default
@click.option('--greeting', default='Hello')
# add a flag (is_flag=True)
@click.option('--caps', is_flag=True)
# the application logic has been refactored into a single function
def hello(**kwargs):
    greeter(**kwargs)

@greet.command()
@click.argument('name')
@click.option('--greeting', default='Goodbye')
@click.option('--caps', is_flag=True)
def goodbye(**kwargs):
    greeter(**kwargs)

if __name__ == '__main__':
    greet()