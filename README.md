# Zadala AWS lambda
Zadala AWS lambda is the lambda handler for [Zadala](https://github.com/RyanAquino/zadala) User login events

### Requirements
- python 3
- AWS account

### Technology
- python 3
- boto3
- AWS Lambda
- AWS DynamoDB
- AWS SQS
- AWS SNS

### Setup
##### create virtual environment
```
python -m venv venv
```

##### Install required packages
```
pip install -r requirements.txt
```

##### Configure AWS 
```
aws configure
```

##### Run lambda handler
```
python main.py
```
