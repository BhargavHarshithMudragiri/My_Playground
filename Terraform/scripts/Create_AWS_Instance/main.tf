provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "terraform_server" {
  ami = var.ami_id_value 
  instance_id = var.instance_id_value
  key_name = var.key_pair_value
  subnet_id = var.subnet_id_value
  tags = {
   Name = "Terraform EC2 Instance"
 }
}

