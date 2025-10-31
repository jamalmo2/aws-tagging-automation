import json
import time

# Simulated AWS data
EC2_INSTANCES = [
    {"InstanceId": "i-0a12b345c678de901", "Region": "us-east-1"},
    {"InstanceId": "i-09f8e7d6c5b4a3210", "Region": "us-west-2"}
]

S3_BUCKETS = [
    {"Name": "demo-app-logs"},
    {"Name": "project-backups"}
]

# Tags you would normally apply in AWS
TAGS = {
    "Environment": "Production",
    "Owner": "DevOps Team",
    "CostCenter": "AWS-Infra",
    "map-migrated": "migW69GT6WKBM"
}

def tag_ec2():
    """Simulates tagging EC2 instances."""
    print("Tagging EC2 instances...")
    for instance in EC2_INSTANCES:
        time.sleep(0.5)
        instance["Tags"] = TAGS
        print(f"Tagged EC2 instance: {instance['InstanceId']} in {instance['Region']}")
    return EC2_INSTANCES

def tag_s3():
    """Simulates tagging S3 buckets."""
    print("Tagging S3 buckets...")
    for bucket in S3_BUCKETS:
        time.sleep(0.5)
        bucket["Tags"] = TAGS
        print(f"Tagged S3 bucket: {bucket['Name']}")
    return S3_BUCKETS

def main():
    print("Starting simulated AWS tagging automation...\n")
    tagged_ec2 = tag_ec2()
    tagged_s3 = tag_s3()

    # Write simulated results to a JSON file
    with open("simulated_tag_results.json", "w") as f:
        json.dump({"EC2": tagged_ec2, "S3": tagged_s3}, f, indent=4)

    print("\nTagging simulation complete. Results saved in simulated_tag_results.json")

if __name__ == "__main__":
    main()
