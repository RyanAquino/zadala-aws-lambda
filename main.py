import json
import boto3


def lambda_handler(event, context):
    dynamodb_client = boto3.resource("dynamodb")
    table = dynamodb_client.Table("UserEvents")
    print(event)

    for record in event.get("Records"):
        print(f"Event source: {record.get('eventSource')}")

        if record.get("eventSource") == "aws:sqs":
            print(f"Message ID: {record.get('messageId')}")

            message_body = json.loads(record.get("body"))
            print(message_body)

            print("Processing message body...")
            body = message_body.get("Message")
            body = json.loads(body)
            user_id = body.get("user_id")
            formatted_record = {
                "UserID": int(user_id) if isinstance(user_id, int) else 0,
                "Event": body.get("event"),
                "Timestamp": body.get("timestamp"),
                "UserAgent": body.get("user_agent"),
                "RemoteAddress": body.get("remote_address"),
            }
            print(formatted_record)

            table.put_item(Item=formatted_record)
            print("Successfully saved to DB")

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}


if __name__ == "__main__":
    event = {}

    lambda_handler(event, None)
