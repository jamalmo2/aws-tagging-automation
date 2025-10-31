# AWS Resource Tagging Automation

A lightweight **Python-based automation script** to tag AWS resources across all regions and services with consistent metadata for cost allocation, compliance, and tracking.

## 🚀 Overview
This project automates the process of adding or updating tags (such as `Environment`, `Owner`, `CostCenter`, or `map-migrated`) on AWS resources like:
- EC2 Instances
- S3 Buckets
- RDS Instances
- EBS Volumes
- Elastic Load Balancers

The script uses the **boto3** library and supports multi-region tagging.

---

## 🧩 Features
✅ Automatically discovers AWS resources  
✅ Tags untagged or incorrectly tagged resources  
✅ Supports multiple AWS regions  
✅ Configurable tag key-value pairs  
✅ Error handling and logging included  

---

## ⚙️ Prerequisites
- Python 3.8+
- AWS credentials configured via CLI or environment variables  
  ```bash
  aws configure
