![Build Status](https://github.com/jamalmo2/aws-tagging-automation/actions/workflows/simulate_tagging.yml/badge.svg?branch=main)

## 🧩 Project Overview
This project simulates AWS resource tagging automation using GitHub Actions and Python — without needing a real AWS account.  
It automatically tags mock EC2 instances and S3 buckets with key metadata such as environment, owner, and cost center, then saves the output as a JSON report.

## ⚙️ How It Works
1. The GitHub Actions workflow (`.github/workflows/simulate_tagging.yml`) runs automatically on every push to `main` or can be triggered manually.
2. It sets up a Python environment in an Ubuntu runner.
3. It runs the `simulate_tag_resources.py` script, which:
   - Tags simulated EC2 instances and S3 buckets.
   - Generates a `simulated_tag_results.json` file.
4. The workflow uploads the JSON report as a downloadable artifact.

## 📊 Results
After the workflow completes successfully:
- A file named `simulated_tag_results.json` is generated.
- You can download it from the GitHub Actions “Artifacts” section.
- The JSON contains structured tagging data, for example:

```json
{
  "EC2": [
    {
      "InstanceId": "i-0a12b345c678de901",
      "Region": "us-east-1",
      "Tags": {
        "Environment": "Production",
        "Owner": "DevOps Team",
        "CostCenter": "AWS-Infra",
        "map-migrated": "migW69GT6WKBM"
      }
    }
  ]
}


---

### 📂 5. Optional — Add “Tech Stack” Section  

```markdown
## 🛠️ Tech Stack
- **Language:** Python 3.10  
- **Automation:** GitHub Actions (CI/CD)  
- **Output:** JSON  
- **OS:** Ubuntu (GitHub Runner)  


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
