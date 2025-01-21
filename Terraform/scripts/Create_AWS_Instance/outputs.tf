output "AWS_Public_Ip" {
 description = "Aws EC2 Instance Public IP Address"
 value = "aws_instance.terraform_server.public_ip"
}
