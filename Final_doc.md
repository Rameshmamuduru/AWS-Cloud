# AWS Compute Services (Clear Explanation + Use Cases)

## 1. EC2 (Elastic Compute Cloud)

### What it is

Virtual server in AWS where you get full control over the machine (like your own computer in the cloud).

### What you manage

Operating system, software, updates, scaling, everything.

### Use cases

- Running web servers like Nginx or Apache
- Hosting backend applications
- Running databases
- Legacy applications that need full OS control

---

## 2. EC2 Auto Scaling

### What it is

Automatically increases or decreases number of EC2 servers based on traffic.

### What it does

- Adds servers when traffic increases
- Removes servers when traffic decreases

### Use cases

High traffic websites
E-commerce applications during sales
Applications with unpredictable traffic

---

## 3. AWS Lambda

### What it is

Serverless service that runs code only when an event happens.

You do not manage servers at all.

### Use cases

- File upload processing in S3
- API backend (serverless APIs)
- Automation scripts
- Event-driven systems like notifications

---

## 4. Elastic Beanstalk

### What it is

A platform where you just upload your application and AWS handles everything else like servers, scaling, and load balancing.

### What AWS manages

EC2, load balancer, scaling, deployment

### Use cases

- Simple web applications
- Startups deploying apps quickly
- Developers who don’t want to manage infrastructure

---

## 5. AWS Lightsail

### What it is

Simple and easy virtual server service with fixed pricing.

It is a simplified version of EC2.

### Use cases

- Small websites
- Blogs (WordPress hosting)
- Learning and basic applications

---

## 6. AWS Batch

### What it is

Service that runs large number of batch jobs automatically.

It handles job scheduling and compute provisioning.

### Use cases

- Video rendering
- Data processing pipelines
- Scientific calculations
- Large file processing jobs

---

## 7. AWS App Runner

### What it is

Fully managed service to deploy web applications or APIs from source code or container.

AWS handles build, deployment, scaling, and networking.

### Use cases

- REST APIs
- Web applications
- Microservices with simple architecture
- Quick deployment from GitHub

---

## 8. AWS Outposts

### What it is

AWS hardware installed inside your own data center.

It brings AWS services on-premise.

### Use cases

- Companies needing hybrid cloud
- Strict data residency rules
- Low latency applications near internal systems

---

## 9. AWS Local Zones

### What it is

Small AWS data centers placed close to major cities for low latency.

### Use cases

- Gaming applications
- Video editing and rendering
- Real-time applications needing fast response

---

## 10. AWS Wavelength

### What it is

AWS infrastructure embedded inside telecom 5G networks.

It brings compute closer to mobile users.

### Use cases

- AR and VR applications
- Autonomous vehicles
- 5G mobile applications
- Real-time streaming apps

---

## 11. AWS Fargate

### What it is

Serverless compute for running containers without managing servers.

You only provide container image and configuration.

### Use cases

- Microservices architecture
- Containerized backend services
- Applications running in ECS or EKS
- Systems where you want no server management

---
---
---

# AWS Storage Services

## 1. Amazon S3 (Simple Storage Service)

### What it is

Object storage service used to store files like images, videos, backups, logs, and documents. Data is stored as objects in buckets.

### Key idea

Highly scalable, durable storage accessible over the internet.

### Use cases

- Storing website images and videos
- Data lakes for analytics
- Application backups
- Log storage
- Static website hosting

---

## 2. Amazon S3 Glacier

### What it is

Low-cost storage designed for long-term archival of data that is rarely accessed.

### Key idea

Very cheap storage but slow retrieval.

### Use cases

- Long-term backups
- Legal and compliance archives
- Historical data storage
- Disaster recovery copies

---

## 3. Amazon EBS (Elastic Block Store)

### What it is

Block storage used with EC2 instances. It acts like a virtual hard disk attached to a server.

### Key idea

Fast, persistent storage for single EC2 instance.

### Use cases

- EC2 root volumes (OS disk)
- Databases running on EC2
- Application storage needing low latency

---

## 4. Amazon EFS (Elastic File System)

### What it is

Shared file storage system that multiple EC2 instances can access at the same time.

### Key idea

A network file system (like shared drive).

### Use cases

- Shared application files across servers
- Web applications with multiple EC2 instances
- Container workloads needing shared storage

---

## 5. Amazon FSx

### What it is

Fully managed high-performance file systems designed for specific workloads.

Types include Windows File Server, Lustre, and NetApp ONTAP.

### Key idea

Specialized enterprise-grade file storage.

### Use cases

- Windows-based applications needing file sharing
- High-performance computing workloads
- Enterprise storage systems

---

## 6. AWS Storage Gateway

### What it is

A hybrid storage service that connects on-premises systems with AWS cloud storage.

### Key idea

Bridge between local data center and AWS storage.

### Use cases

- Backing up on-premises data to AWS S3
- Migrating data to cloud gradually
- Hybrid cloud storage setups
- Archiving on-prem data to Glacier

---

## 7. AWS Backup

### What it is

Centralized backup service to automate and manage backups across multiple AWS services.

### Key idea

One place to manage all backups.

### Supports

EBS, EFS, RDS, DynamoDB, FSx

### Use cases

- Automated backup scheduling
- Disaster recovery planning
- Compliance and audit requirements
- Centralized backup management across AWS


