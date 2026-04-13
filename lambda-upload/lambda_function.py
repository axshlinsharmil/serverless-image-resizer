import boto3
import base64
import uuid

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        image_data = base64.b64decode(event['body'])

        file_name = str(uuid.uuid4()) + ".jpg"

        s3.put_object(
            Bucket='image-resizer-buckets',
            Key='original/' + file_name,
            Body=image_data,
            ContentType='image/jpeg'
        )

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': 'Upload successful'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }