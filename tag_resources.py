import boto3
from botocore.exceptions import ClientError

# Define the tags you want to apply to AWS resources
TAGS = {
    "Environment": "Production",
    "Owner": "DevOps Team",
    "CostCenter": "AWS-Infra",
    "map-migrated": "migW69GT6WKBM"
}

def tag_ec2(region):
    """
    This function tags all EC2 instances in a given AWS region.
    """
    ec2 = boto3.client("ec2", region_name=region)
    instances = ec2.describe_instances()

    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            try:
                ec2.create_tags(
                    Resources=[instance_id],
                    Tags=[{"Key": k, "Value": v} for k, v in TAGS.items()]
                )
                print(f"Tagged EC2 instance: {instance_id}")
            except ClientError as e:
                print(f"Could not tag {instance_id}: {e}")

def tag_s3():
    """
    This function tags all S3 buckets in your AWS account.
    """
    s3 = boto3.client("s3")
    buckets = s3.list_buckets()["Buckets"]

    for bucket in buckets:
        name = bucket["Name"]
        try:
            s3.put_bucket_tagging(
                Bucket=name,
                Tagging={"TagSet": [{"Key": k, "Value": v} for k, v in TAGS.items()]}
            )
            print(f"Tagged S3 bucket: {name}")
        except ClientError as e:
            print(f"Could not tag {name}: {e}")

def main():
    """
    Main entry point for the script.
    It loops through all AWS regions and calls the tagging functions.
    """
    print("Starting AWS tagging automation...")

    ec2_client = boto3.client("ec2")
    regions = [r["RegionName"] for r in ec2_client.describe_regions()["Regions"]]

    for region in regions:
        print(f"Processing region: {region}")
        tag_ec2(region)

    tag_s3()
    print("Tagging complete.")

if __name__ == "__main__":
    main()
