# \# Serverless Feedback Collector

# 

# \## Project Overview

# A fully serverless feedback collection application built on AWS cloud services. This project demonstrates a decoupled, scalable architecture that processes user feedback through multiple AWS services without managing any servers.

# 



\## Live Demo

\*\*Access the application here:\*\* \[Your Static Website URL]



\## AWS Services Used

\- \*\*Amazon S3\*\* - Static website hosting

\- \*\*Amazon API Gateway\*\* - REST API endpoint

\- \*\*Amazon SQS\*\* - Message queue for decoupling

\- \*\*AWS Lambda\*\* - Serverless compute (Python)

\- \*\*Amazon DynamoDB\*\* - NoSQL database

\- \*\*Amazon SNS\*\* - Email notifications

\- \*\*AWS IAM\*\* - Security and permissions

\- \*\*AWS CloudFormation\*\* - Infrastructure as Code



\## Technical Stack

\- \*\*Python 3.12\*\* - Lambda functions

\- \*\*JavaScript\*\* - Frontend logic

\- \*\*HTML/CSS\*\* - User interface

\- \*\*JSON\*\* - CloudFormation templates



\## Features

\-  \*\*100% Serverless\*\* - No servers to manage

\-  \*\*Auto-scaling\*\* - Handles traffic spikes automatically

\-  \*\*Cost Effective\*\* - Free Tier friendly

\-  \*\*Real-time Processing\*\* - Asynchronous workflow

\-  \*\*Email Notifications\*\* - Instant admin alerts

\-  \*\*Secure\*\* - IAM roles with least privilege



\## Data Flow

1\. \*\*Frontend\*\*: User submits feedback through S3-hosted website

2\. \*\*API Gateway\*\*: Receives HTTP POST requests

3\. \*\*SQS Queue\*\*: Buffers requests for reliability

4\. \*\*Process Lambda\*\*: Stores feedback in DynamoDB

5\. \*\*DynamoDB\*\*: Persists data with automatic streaming

6\. \*\*Notify Lambda\*\*: Sends email via SNS

7\. \*\*SNS\*\*: Delivers notifications to administrators





\## Deployment

\- \*\*Infrastructure as Code\*\*: CloudFormation templates

\- \*\*Manual Setup\*\*: S3 static website hosting

\- \*\*Automated\*\*: Lambda deployments via S3



\## Technical Highlights

\- Event-driven architecture

\- CORS configuration for web security

\- Comprehensive error handling

\- CloudWatch logging and monitoring

\- Cost-optimized for Free Tier



\## Scalability

\- \*\*Frontend\*\*: Unlimited users via S3

\- \*\*API\*\*: 10,000+ RPS via API Gateway

\- \*\*Processing\*\*: Concurrent Lambda executions

\- \*\*Storage\*\*: Unlimited DynamoDB capacity



\## Learning Outcomes

\- AWS serverless service integration

\- CloudFormation template development

\- Python Lambda programming

\- Event-driven architecture patterns

\- CORS and web security

\- AWS cost optimization



---

