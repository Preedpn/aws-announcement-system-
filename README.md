# Web-Based Announcement Broadcasting System  
Using AWS API Gateway, Lambda, and Amazon SNS

This project is a simple, scalable **announcement broadcasting system** that allows a user to send a message from a **web interface** and deliver it instantly to **all subscribed email users** using AWS services.

The system uses:
- **HTML/JavaScript Web UI**  
- **Amazon API Gateway**  
- **AWS Lambda (Python)**  
- **Amazon SNS (Email Notifications)**  

---

## 🚀 Features
- Send announcements from any browser  
- Instantly broadcast messages to all subscribers  
- Fully serverless architecture  
- Secure, scalable, and cost-efficient  
- Uses SNS for email delivery  
- Includes CORS handling for smooth web access  

---

## 📌 Architecture Diagram

![Architecture Diagram](./architecture-diagram.png)

> Replace the above with your actual PNG diagram.

---

## 🏗️ System Architecture (Explained)
1. **Web UI (announcement.html)**  
   User enters the announcement message and clicks **Send**.

2. **API Gateway**  
   Receives the request and forwards it to Lambda.  
   Configured with:
   - POST method  
   - CORS enabled  
   - `/announcement` endpoint  

3. **AWS Lambda**  
   Processes the incoming request and publishes the message to SNS.

4. **Amazon SNS (Simple Notification Service)**  
   Broadcasts the announcement to all email subscribers under the topic.

---

## 📂 Project Structure
├── announcement.html
├── lambda_function.py
├── README.md
└── architecture-diagram.png
# 🔧 Setup Instructions

### **1. Create an SNS Topic**
1. Go to AWS SNS  
2. Create a Topic → Standard  
3. Note the **Topic ARN**  
4. Add email subscriptions  
5. Confirm subscription via email

---

### **2. Create Lambda Function**
- Runtime: **Python 3.x**
- Add environment variable:

| Key              | Value                    |
|------------------|--------------------------|
| SNS_TOPIC_ARN    | arn:aws:sns:REGION:ID:TopicName |

- Add this IAM permission to Lambda role:
