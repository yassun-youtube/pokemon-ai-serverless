import json
import boto3

dynamodb = boto3.resource('dynamodb')

def hello(event, context):
    return {"statusCode": 200, "body": "Hello World"}
    # route_key = event['requestContext']['routeKey']
    #
    # if route_key == "$connect":
    #     return handle_connect(event)
    # elif route_key == "$disconnect":
    #     return handle_disconnect(event)
    # elif route_key == "sendMessage":
    #     return handle_send_message(event)
    # elif route_key == "heartbeat":
    #     return handle_heartbeat(event)
    # else:
    #     return {"statusCode": 500, "body": "Unrecognized route"}


def connect(event, context):
    connection_id = event['requestContext']['connectionId']
    print(f"Connection ID: {connection_id}")

    table = dynamodb.Table('ConnectionId')
    table.put_item(Item={
        'player': 'yassun',
        'connectionId': connection_id,
    })

    # 接続時の処理
    return {"statusCode": 200, "body": "Connected"}


def disconnect(event, context):
    # 切断時の処理
    return {"statusCode": 200, "body": "Disconnected"}

def default(event, context):
    # 切断時の処理
    return {"statusCode": 200, "body": "Default"}


def handle_send_message(event, context):
    # メッセージ受信時の処理
    data = json.loads(event['body'])
    # メッセージの処理ロジック
    return {"statusCode": 200, "body": "Message received"}


def heartbeat(event, context):
    # ハートビートメッセージの処理
    return {"statusCode": 200, "body": "Heartbeat acknowledged"}
