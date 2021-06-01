import json
import boto3

def handler(event, context):
    # Create SQS client. Uncomment when the creation of the real application will be started.
    # sqs = boto3.client('sqs')
    # return json.dumps(sqs)

    # queue_url = 'https://sqs.eu-central-1.amazonaws.com/254685023080/myelsk-sqs'

    # message = {"key": "value"}
    # response = sqs.send_message(
        #QueueUrl="https://sqs.eu-central-1.amazonaws.com/254685023080/myelsk-sqs",
        #MessageBody=json.dumps(message)
    # )

    # return {
        #'statusCode': 200,
        #'body': json.dumps(response)
    # }
    return {
      'statusCode': 200,
      'body': json.dumps('Hello fom first layer handler!')
    }