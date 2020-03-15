#!/usr/bin/python
import re

# Creating empty Employee details dictionary
employee_details = {}

# error handling and emp id validation block
try:
    emp_id = int(input("What's Employee ID: should be of 6 digits: "))
    result = re.match(r"\d{6}$", str(emp_id))
    if result:
        pass
    else:
        exit("6 digit emp id please")
except Exception as e:
    exit("Need only integer: {}".format(e))

# error handling and emp name validation block
try:
    emp_name = input("Please enter employee name: ")
    result = re.match(r"([a-zA-Z]+((['. ][a-zA-Z ])?[a-zA-Z]?)+)$", str(emp_name))
    if result:
        pass
    else:
        exit("Not a valid name, it seems")
except Exception as e:
    exit("Are you sure, you typed only name: {}".format(e))

# error handling and join date validation block in the format yyyy-mm-dd
try:
    join_date = input("Please enter joining date in format yyyy-mm-dd: ")
    result = re.match(r"\d{4}-\d{2}-\d{2}$", str(join_date))
    if result:
        pass
    else:
        exit("Not a valid date, it seems")
except Exception as e:
    exit("Are you sure, you typed correct joining date: {}".format(e))

skills_list = input("Enter skill(s) separated by comma (,): ")
skills_list = skills_list.split(",")

projects_list = input("Enter project(s) details in the format. project_name: project_description ")
project, project_description = projects_list.split(":")
projects = {project: project_description}

employee_details = {
    emp_id:{
        'name': emp_name,
        'joining date': join_date,
        'skills': skills_list,
        'projects': projects
    }
}

print(employee_details)