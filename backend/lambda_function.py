import json
import boto3
import os

# --- CONFIGURATION ---
# For security, we read the ARN from Environment Variables.
# In AWS Lambda Console -> Configuration -> Environment variables, set:
# Key: SNS_TOPIC_ARN
# Value: arn:aws:sns:region:account-id:topic-name
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN')
# ---------------------

sns_client = boto3.client('sns')

def lambda_handler(event, context):
    print("DEBUG: Function started")
    
    try:
        # 1. Parse the Request Body
        if 'body' in event and event['body']:
            if isinstance(event['body'], str):
                body = json.loads(event['body'])
            else:
                body = event['body']
        else:
            body = event 

        subject = body.get('subject', 'Announcement')
        message = body.get('message')

        # 2. Validate Input
        if not message:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*', # Required for CORS
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({'error': 'Message field is required'})
            }

        # 3. Publish to Amazon SNS
        response = sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=subject,
            Message=message
        )
        
        # 4. Return Success Response
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*', # Required for CORS
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'status': 'Success', 
                'messageId': response['MessageId']
            })
        }

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': str(e)})
        }