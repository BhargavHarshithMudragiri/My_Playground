variable "ami_id" {
  description = "EC2 Instance AMI ID"
  type = string
}

variable "instance_id" {
  description = "EC2 Instance Type"
  type = string
}

variable "key_pair" {
  description = "EC2 Instance Key Pair"
  type = string
}

variable "subnet_id" {
  description = "EC2 Instance Subnet_Id"
  type = string
}

variable "bucket_name" {
  description = "AWS S3 Bucket name"
  type = string
}

varibale "dynamodb" {
  description = "AWS Dynamo DB Name"
  type = string
}
