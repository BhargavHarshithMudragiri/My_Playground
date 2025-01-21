provider "aws" {
 region = "us-east-1"
 alias = "East_Region"
}

provider "aws" {
 region = "us-west-1"
 alias = "West_Region
}

resource "aws_instance" "Terraform_Instance" {
 ami = var.ami_id
 instance_type = var.instance_type_id
 provider = aws.East_Region
 key_name = var.key_pair
 subnet_id = var.subnet_id
 tags = {
   Name = "Test-Terraform-Server"
   Environment = "development"
   }
}

resource "aws_s3_bucket" "test-s3-bucket" {
  bucket = var.bucket_name
  provider = aws.East_Region
}

resource "aws_dynamodb_table" "test-dynamo-db" {
  name = var.dynamodb
  provider = aws.West_Region
  billing_mode = "PAY_PER_REQUEST"
  hask_key = "LockId"

  attribute {
    name = "LockId"
    type = "S"
   }
}
