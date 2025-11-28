```markdown
# Web-Based Announcement Broadcasting System  
Using AWS API Gateway, Lambda, and Amazon SNS

This project allows users to send announcements from a simple web interface and broadcast them instantly to all subscribers via email using AWS services. It is fully serverless, scalable, and easy to deploy.

---

## 🚀 Features
- Send announcements through a web page  
- Emails delivered to all subscribed users  
- Serverless architecture (no servers needed)  
- Secure and highly scalable  
- Low cost and easy to maintain  

---

## 📌 Architecture Diagram
(Add your diagram here)

---

## 🏗️ System Workflow
1. User enters a message in **announcement.html**  
2. API Gateway receives the POST request  
3. Lambda function processes the message  
4. Lambda publishes it to an SNS topic  
5. SNS sends email to all subscribed email addresses  

---

## 📂 Project Structure
```

├── announcement.html
├── lambda_function.py
├── README.md
└── architecture-diagram.png

```

---

## 🔧 Setup Instructions

### 1. Create SNS Topic
- Create a **Standard** SNS topic  
- Copy the **Topic ARN**  
- Add email subscriptions and confirm them  


### 2. Create Lambda Function
- Runtime: **Python 3.x**
- Add environment variable:

| Key           | Value (example) |
|---------------|------------------|
| SNS_TOPIC_ARN | arn:aws:sns:region:account-id:TopicName |

- Add permission to Lambda role:
```

SNS:Publish

````

#### Lambda Code
```python
import json
import boto3
import os

SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")
sns_client = boto3.client("sns")

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        message = body.get("message", "")
        
        response = sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject="New Announcement"
        )
        
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST,OPTIONS",
                "Access-Control-Allow-Headers": "*"
            },
            "body": json.dumps({"status": "Message sent"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
````

---

### 3. API Gateway Setup

* Create **REST API**
* Create resource: `/announcement`
* Create **POST** method → Integrate with Lambda
* Enable **CORS**
* Deploy API
* Copy the **Invoke URL**

---

### 4. Update HTML File

Replace API URL inside `announcement.html`:

```javascript
const API_URL = "YOUR_API_GATEWAY_ENDPOINT";
```

---

### 5. Use the Application

* Open `announcement.html`
* Type your message
* Click **Send Announcement**
* All subscribers receive the email

---

## 📜 License

Open-source project. Free to use and modify.

```
```
