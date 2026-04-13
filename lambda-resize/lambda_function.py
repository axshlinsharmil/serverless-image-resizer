import boto3
from PIL import Image
import io
import urllib.parse

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    if not key.startswith('original/'):
        return

    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        image_content = response['Body'].read()

        img = Image.open(io.BytesIO(image_content))
        img = img.resize((300, 300))

        buffer = io.BytesIO()
        img.save(buffer, format='JPEG', quality=70)
        buffer.seek(0)

        new_key = key.replace('original/', 'resized/')

        s3.put_object(
            Bucket=bucket,
            Key=new_key,
            Body=buffer,
            ContentType='image/jpeg'
        )

        print("Resized successfully")

    except Exception as e:
        print(e)
        raise e