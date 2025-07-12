Firebase Cloud Firestore API Exercise
This repository documents the process of setting up a NoSQL database (Cloud Firestore), adding data, and retrieving a single record via its REST API. This is part of my AI Native Journey, demonstrating fundamental backend interaction.

1. Firebase Project Setup
Project Name: MyDatabaseApp (or whatever you named your Firebase project)

Project ID: mydatabaseapp-6c085 (Replace with your actual Project ID from Firebase Project Settings)

Database Type: Cloud Firestore (NoSQL, document-oriented)

Initial Mode: Started in "test mode" for demonstration purposes.

2. Cloud Firestore Database Setup & Data Entry
Collection: products
A collection named products was created to store product information.

Documents (Entries):
Three documents were manually added to the products collection, each with an auto-generated ID.

Document 1 (Laptop):
{
  "name": "Laptop",
  "price": 1200,
  "inStock": true
}

Document 2 (Smartphone):
{
  "name": "Smartphone",
  "price": 700,
  "inStock": true
}

Document 3 (Headphones):
{
  "name": "Headphones",
  "price": 150,
  "inStock": false
}

3. Firebase Security Rules for Public Read Access
IMPORTANT SECURITY WARNING: The following rule allows anyone on the internet to read your entire database. This is highly insecure for production applications and should only be used for learning and demonstration purposes. For a real application, you would implement much more restrictive rules based on user authentication and authorization.

The Firestore security rules were modified to allow public read access:

rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read: if true;  // Allows anyone to read data
      allow write: if false; // Keeps write access restricted
    }
  }
}

4. Retrieving a Record via REST API
API Call Used:
To retrieve a specific document (e.g., the "Laptop" document) from the products collection:

GET https://firestore.googleapis.com/v1/projects/mydatabaseapp-6c085/databases/(default)/documents/products/zkbvW1cp8zpZVmqw7sx6

(Remember to replace mydatabaseapp-6c085 with your actual Firebase Project ID and zkbvW1cp8zpZVmqw7sx6 with the exact Document ID from your successful API call.)

Successful JSON Response Received:
This is the actual JSON response received when the above API call was executed successfully:

{
  "name": "projects/mydatabaseapp-6c085/databases/(default)/documents/products/zkbvW1cp8zpZVmqw7sx6",
  "fields": {
    "inStock": {
      "booleanValue": true
    },
    "price": {
      "integerValue": "1200"
    },
    "name": {
      "stringValue": "Laptop"
    }
  },
  "createTime": "2025-07-12T16:05:16.265244Z",
  "updateTime": "2025-07-12T16:05:16.265244Z"
}

5. The Point of This Exercise
This exercise serves as a practical demonstration of several core concepts in modern application development:

Backend-as-a-Service (BaaS): Utilizing a managed cloud service like Firebase to handle backend infrastructure (database, authentication, etc.), allowing developers to focus on application logic rather than server management.

NoSQL Data Modeling: Understanding the flexible, document-oriented approach of NoSQL databases, where data is stored in JSON-like documents within collections.

API Interaction: Learning how applications communicate with backend services using standardized Application Programming Interfaces (APIs), specifically through RESTful HTTP requests. This enables the frontend to request and receive data from the backend.

Dynamic Content: The ability to fetch and display data dynamically based on user interactions or application needs, which is crucial for building interactive and responsive web and mobile applications.

Database Security: Grasping the importance of security rules to control access to your data, even while demonstrating how to temporarily open access for testing.

This entire process is a foundational step in understanding how data flows in a typical web or mobile application, from storage to retrieval.