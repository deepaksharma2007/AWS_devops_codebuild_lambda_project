import json

def deepak(event, context):
    # TODO implement
 
 print("Hello I am Deepak")
 
 return {
        'statusCode': 200,
        'body': json.dumps('Hello from deepak & the code build successfully to lambda function !! ')
    }
