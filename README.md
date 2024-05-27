![image](https://github.com/Aditi55Pathak/EBS-Python-for-hosting/assets/80877301/d6feca75-32b4-4e5f-ad84-baebd6ddf7ac)# CI/CD Hosting on Elastic Beanstalk

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

![image](https://github.com/Aditi55Pathak/EBS-Python-for-hosting/assets/80877301/5ec6c3bc-0128-40b7-944a-89cea15f8610)

![image](https://github.com/Aditi55Pathak/EBS-Python-for-hosting/assets/80877301/f6638fe6-3d8c-4092-9dab-272da387f70f)

![image](https://github.com/Aditi55Pathak/EBS-Python-for-hosting/assets/80877301/e494b424-fa09-4783-b54f-0afee253ec01)



### 3. Set Up AWS Elastic Beanstalk
Go to the AWS Management Console and set up Elastic Beanstalk:
- Create a new Elastic Beanstalk environment.
- Choose the appropriate platform (e.g., Python).
- Upload your application code or connect it to your GitHub repository.


![image](https://github.com/Aditi55Pathak/EBS-Python-for-hosting/assets/80877301/8e70a6e1-82e0-47e7-9b77-a1727c0ac7a1)

![image](https://github.com/Aditi55Pathak/EBS-Python-for-hosting/assets/80877301/0a02d0a7-5ef8-4ab1-b372-19a4e8f6618e)

![image](https://github.com/Aditi55Pathak/EBS-Python-for-hosting/assets/80877301/b23779a4-c7d0-45b3-a00d-2aea19abe648)




### 4. Set Up AWS CodePipeline
Navigate to the AWS CodePipeline service and create a new pipeline:
- Connect the pipeline to your GitHub repository.
- Set up the build and deploy stages using AWS CodeBuild and Elastic Beanstalk.
- Configure the necessary buildspec.yml file if needed.

![image](https://github.com/Aditi55Pathak/EBS-Python-for-hosting/assets/80877301/8b4bb9a2-c5e9-491c-9897-6ae974287f1d)


### 5. Automate Your Code with Elastic Beanstalk
Once the pipeline is set up, any changes pushed to your GitHub repository will automatically trigger the pipeline to build and deploy the updated code to your Elastic Beanstalk environment.

![image](https://github.com/Aditi55Pathak/EBS-Python-for-hosting/assets/80877301/fc31716f-9983-40a3-a052-58bcfcce14a2)



## Conclusion
With this setup, you can achieve a fully automated CI/CD pipeline for your Python application with a MySQL database, hosted on AWS Elastic Beanstalk. This ensures that your application is always up-to-date with the latest changes from your GitHub repository, providing a seamless deployment process.
