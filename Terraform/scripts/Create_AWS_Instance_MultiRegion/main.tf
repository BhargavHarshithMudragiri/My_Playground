provider "aws" {
  region="us-east-1"
}

module "AWS_Resource_Creation" {
  source = "./modules/AWS_Resource_Creation"
  ami_id = "ami-04b4f1a9cf54c11d0"
  instance_type = "t2.micro"
  key_name = "aws_key"
  subnet_id = "subnet-0a529a9d0dc65f1b0"
  bucket_name = "aws-s3-test-bucket-store"
  dynamodb = "test_dynamo_db"
}

