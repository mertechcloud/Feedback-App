import json

import boto3

import os


sns = boto3.client('sns')


def lambda_handler(event, context):

    sns_topic_arn = os.environ['SNS_TOPIC_ARN']

    notifications_sent = 0

    

    for record in event['Records']:

        if record['eventName'] == 'INSERT':

            try:

                new_image = record['dynamodb']['NewImage']

                feedback_id = new_image['feedback_id']['S']

                feedback_text = new_image['feedback']['S']

                user_email = new_image.get('email', {}).get('S', 'anonymous')

                timestamp = new_image['timestamp']['S']

                

                message = f"""New Feedback Received!


Feedback ID: {feedback_id}

From: {user_email}

Time: {timestamp}

Feedback: {feedback_text}


---

AWS Serverless Feedback App"""

                

                sns.publish(

                    TopicArn=sns_topic_arn,

                    Message=message,

                    Subject='New Feedback Received'

                )

                notifications_sent += 1

                

            except Exception as e:

                print(f'Error: {str(e)}')

    

    return {

        'statusCode': 200,

        'body': json.dumps({'message': f'Sent {notifications_sent} notifications'})

    }
