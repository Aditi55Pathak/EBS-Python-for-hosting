# CI/CD Hosting on Elastic Beanstalk

## Project Overview
This project demonstrates how to automate the deployment of a Python application with a MySQL database to AWS Elastic Beanstalk using AWS CodePipeline. The goal is to set up a continuous integration and continuous deployment (CI/CD) pipeline that automatically deploys your code whenever changes are pushed to your GitHub repository.

## Tools
- GitHub
- AWS CodePipeline
- AWS Elastic Beanstalk

## Procedure

### 1. Create a GitHub Repository
First, create a new repository on GitHub for the project you want to host. Push your application code to this repository.
![image](https://github.com/Aditi55Pathak/EBS-Python-for-hosting/assets/80877301/da5b62ef-3264-4e3c-b0ef-f796aeaf072b)

### 2. Set Up Code and Database
Ensure your Python application is set up with a MySQL database. You should have a working configuration that can connect to the database and perform the necessary operations.

### 3. Set Up AWS Elastic Beanstalk
Go to the AWS Management Console and set up Elastic Beanstalk:
- Create a new Elastic Beanstalk environment.
- Choose the appropriate platform (e.g., Python).
- Upload your application code or connect it to your GitHub repository.

### 4. Set Up AWS CodePipeline
Navigate to the AWS CodePipeline service and create a new pipeline:
- Connect the pipeline to your GitHub repository.
- Set up the build and deploy stages using AWS CodeBuild and Elastic Beanstalk.
- Configure the necessary buildspec.yml file if needed.

### 5. Automate Your Code with Elastic Beanstalk
Once the pipeline is set up, any changes pushed to your GitHub repository will automatically trigger the pipeline to build and deploy the updated code to your Elastic Beanstalk environment.


## Conclusion
With this setup, you can achieve a fully automated CI/CD pipeline for your Python application with a MySQL database, hosted on AWS Elastic Beanstalk. This ensures that your application is always up-to-date with the latest changes from your GitHub repository, providing a seamless deployment process.
