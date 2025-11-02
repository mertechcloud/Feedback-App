import json

import boto3

import uuid

from datetime import datetime

import os


dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):

    table_name = os.environ['DYNAMODB_TABLE']

    table = dynamodb.Table(table_name)

    processed_count = 0

    

    for record in event['Records']:

        try:

            body = json.loads(record['body'])

            feedback_text = body.get('feedback', '').strip()

            user_email = body.get('email', 'anonymous').strip()

            

            if not feedback_text:

                continue

                

            item = {

                'feedback_id': str(uuid.uuid4()),

                'feedback': feedback_text,

                'email': user_email,

                'timestamp': datetime.utcnow().isoformat(),

                'status': 'received'

            }

            

            table.put_item(Item=item)

            processed_count += 1

            

        except Exception as e:

            print(f'Error: {str(e)}')

    

    return {

        'statusCode': 200,

        'body': json.dumps({'message': f'Processed {processed_count} feedback items'})

    }
