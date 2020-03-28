# AWS Lab Practice
## You will see lots of lab with step-by-step instructions

*You will get lots of scenario based examples in this repo.*

**Python Lab Practice**

1. Create a Dictionary for employees

*Structure:*
```
{ 'Employee ID':
	{ 	Name: ''
		Joined: 'yyyy-mm-dd'
		Skills: []
		Project: {}
	}
}
```
*Helpful Steps*
1. use input function to get those details form user
2. use basic regular expression for name and id validation
4. Use try except block for error handling
5. Do some basic validation on those inputs

*Optional*
1. Define a function to pass Employeed details (input) and create a dictionary
2. Function to list employee details: pass employee ID as an argument
3. pass emp id and specific info that you want to print
4. Function to add/update/delete employee details

## AWS Lab Practice (CLI and Boto3)
1. Setup AWS CLI and run `aws s3 ls`

2. Print all regions
    * `aws ec2 describe-regions`
    * `aws ec2 describe-regions --query "Regions[].{Name:RegionName}" --output text`

3. List EC2 running instances region wise
    * `aws ec2 describe-instances`
    * `aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId]' --filters Name=instance-state-name,Values=running --output text	`
    * loop through the regions
4. EC2 and security group
    * Print Security group name attached with each ec2 instances using filters
    * Print security group name with ingress rules attached with each ec2 instances
5. S3 manipulation
    * List all s3 buckets: `aws s3 ls`
    * List only public s3 buckets: `aws s3api get-bucket-policy --bucket video-dlwd` can help
    * download bucket files: `aws s3 sync s3://video-dlwd .`
    * Get bucket policy: `aws s3api get-bucket-policy --bucket video-dlwd --query Policy --output text > policy.json`
    * Get bucket location: `aws s3api get-bucket-location --bucket video-dlwd`

6. Get IAM user details: `aws iam list-users`


# BONUS
## Example of click
```
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
```