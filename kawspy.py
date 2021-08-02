import boto3
iotanalytics = boto3.client("iotanalytics")
sns = boto3.client("sns")
from os import environ
ddb = boto3.client("dynamodb")
translate = boto3.client("translate")

def handler(event, context):
        
        try:
            data = ddb.scan(
                TableName="KChineseAnimal"
            )
            print(data)
        except BaseException as e:
            print(e)
            raise(e)
            try:
                data = sns.get_topic_attributes(
                    TopicArn="arn:aws:sns:us-east-1:318300609668:Notifications"
                )
                print(data)
            except BaseException as e:
                print(e)
                raise(e)
                try:
                    data = iotanalytics.batch_put_message(
                        channelName="my_channel",
                        messages=[
                            {
                                'messageId': "ID",
                                'payload': "Test Message"
                            }
                        ]
                    )
                    print(data)
                except BaseException as e:
                    print(e)
                    raise(e)
    
    return {"message": "Successfully executed"}
