# 🌐 Google Cloud Platform (GCP) Overview

## Table of Contents
1. [Introduction to GCP](#introduction-to-gcp)
2. [Global Footprint and services](#global-footprint-and-services)
   - [Regions](#regions)
   - [Zones](#zones)
   - [Network & Edge Locations](#network--edge-locations)
   - [Available Countries & Territories](#24-available-countries--territories)
3. [Interacting with GCP](#interacting-with-gcp)
   - [Web Console](#web-console)
   - [Cloud Shell](#cloud-shell)
   - [Mobile App](#mobile-app)
   - [REST APIs](#rest-apis)
4. [Core Building Blocks](#core-building-blocks-of-gcp)
   - [Compute Services](#compute-services)
   - [Storage Services](#storage-services)
   - [Networking Services](#networking-services)
   - [Identity and Access Management (IAM)](#identity-and-access-management-iam)

---

## Introduction to GCP

Google Cloud Platform (GCP) is a suite of cloud services that enables developers and enterprises to build, deploy, and scale applications on Google's infrastructure. It supports a wide range of services including compute, storage, networking, machine learning, and security.

Google Cloud Platform is organized hierarchically to support scalable and secure resource management:
- Organization: Top-level container for resources
- Folders: Optional grouping of projects for policy inheritance
- Projects: Core unit for billing, permissions, and resource management
- Resources: Actual services and components (VMs, storage, etc.)
This structure enables efficient governance, access control, and billing across teams and environments.

---

## Global Footprint and Services

GCP spans over 200 countries and territories, with a robust infrastructure of:
- 40+ regions
- 120+ zones
- 200+ edge locations
- Offers 100+ services across domains such as:
  - Infrastructure
  - Databases
  - Analytics
  - AI/ML
  - Security
  - DevOps
    
This global presence ensures high availability, low latency, and compliance with regional data regulations.

### Regions
Regions are independent geographic areas where GCP resources are hosted.

| Region Name            | Location           |
|------------------------|--------------------|
| `us-central1`          | Iowa, USA          |
| `asia-south1`          | Mumbai, India      |
| `europe-west2`         | London, UK         |
| `australia-southeast1` | Sydney, Australia  |
| `southamerica-east1`   | São Paulo, Brazil  |


### Zones
Zones are deployment areas within regions. Each region typically has 3 or more zones (e.g., `us-central1-a`, `us-central1-b`).

Zones provide fault isolation and high availability for workloads.


### Network & Edge Locations
- **Private Global Fiber Network**: Connects all regions with low latency.
- **Edge Locations**: 200+ worldwide for CDN, DNS, and load balancing.
- **Purpose**: Deliver content faster and improve reliability.


### Available Countries & Territories
GCP is available in over 200 countries and territories, including:
- 🇮🇳 India
- 🇺🇸 USA
- 🇯🇵 Japan
- 🇦🇺 Australia
- 🇧🇷 Brazil
- 🇬🇧 UK
- 🇩🇪 Germany
- 🇨🇦 Canada
- 🇸🇬 Singapore
- 🇫🇷 France

---


## Interacting with GCP

There are various ways users can **access, manage, and control cloud resources and services**. 
Whether you're deploying applications, configuring infrastructure, monitoring usage, or automating tasks, GCP provides multiple interfaces to suit different workflows and preferences.
These interaction methods range from **graphical user interfaces (GUIs)** for ease of use, to **command-line tools** and **programmatic APIs** for automation and integration.


### Web Console
- Accessible at [https://console.cloud.google.com](https://console.cloud.google.com)
- GUI-based interface for managing resources
- Ideal for quick configuration, monitoring, and billing

### Cloud Shell
- Browser-based command-line interface
- Comes with pre-installed SDKs and tools
- Persistent 5 GB home directory
- Great for scripting, automation, and CLI access
  
### Mobile App
- Available on Android and iOS
- Monitor resources, receive alerts, and manage billing
- Limited functionality compared to Web Console
  
### REST APIs
- Programmatic access to GCP services
- Use with tools like `curl`, Postman, or custom apps
- Requires authentication via OAuth 2.0 or service accounts
- API Explorer: [https://cloud.google.com/apis](https://cloud.google.com/apis)

---


# Core Building Blocks of GCP

Google Cloud Platform offers a wide range of services grouped into foundational categories: **Compute**, **Storage**, **Networking**, and **Identity & Access Management (IAM)**. 
These building blocks enable developers and organizations to build scalable, secure, and efficient cloud-native applications.

## Compute Services

These services provide the processing power to run applications and workloads.

| Service | Description |
|--------|-------------|
| **Compute Engine** | Infrastructure as a Service (IaaS) offering virtual machines with customizable configurations. |
| **Google Kubernetes Engine (GKE)** | Managed Kubernetes service for orchestrating containerized applications. |
| **Cloud Run** | Serverless platform for running stateless containers triggered by HTTP requests. |
| **Cloud Functions** | Lightweight, event-driven serverless functions for microservices and automation. |
| **App Engine** | Platform-as-a-Service (PaaS) for deploying web applications without managing infrastructure. |


## Storage Services

These services handle data persistence across various formats and access patterns.

| Service | Type | Use Case |
|--------|------|----------|
| **Cloud Storage** | Object | Scalable storage for unstructured data like images, videos, and backups. |
| **Persistent Disk** | Block | Durable block storage for Compute Engine VMs. |
| **Filestore** | File | Managed NFS file storage for applications requiring shared file systems. |
| **Cloud SQL** | Relational | Managed relational databases (MySQL, PostgreSQL, SQL Server). |
| **Bigtable** | NoSQL | High-throughput NoSQL database for time-series and IoT data. |
| **Firestore** | NoSQL | Document-based database for mobile and web apps. |
| **BigQuery** | Data warehouse | Serverless analytics platform for large-scale data queries. |

## Networking Services

These services enable secure and scalable connectivity between resources and users.

| Feature | Purpose |
|--------|---------|
| **VPC (Virtual Private Cloud)** | Create isolated, customizable networks for GCP resources. |
| **Cloud Load Balancing** | Distribute traffic across multiple instances globally. |
| **Cloud CDN** | Cache content at edge locations to reduce latency and improve performance. |
| **Cloud Interconnect** | Establish high-speed, private connections between on-prem and GCP. |
| **Cloud DNS** | Scalable, reliable domain name resolution service. |


## Identity and Access Management (IAM)

These tools help manage user identities, permissions, and security policies.

| Tool | Function |
|------|----------|
| **IAM (Identity and Access Management)** | Assign roles and permissions to users and service accounts. |
| **Cloud Identity** | Manage user identities and authentication across GCP services. |
| **Secret Manager** | Securely store and access sensitive data like API keys and credentials. |
| **Security Command Center** | Centralized visibility into security risks and compliance posture. |
| **BeyondCorp** | Implement zero-trust access controls for secure resource access. |

---

