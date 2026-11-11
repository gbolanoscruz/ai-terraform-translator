terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configuramos el proveedor de AWS
provider "aws" {
  region = "us-east-1"
}

# Creamos una instancia EC2 básica
resource "aws_instance" "mi_servidor_web" {
  ami           = "ami-0c55b159cbfafe1f0" # Amazon Linux 2 AMI
  instance_type = "t2.micro"

  tags = {
    Name        = "ServidorWeb-Produccion"
    Environment = "Prod"
    Owner       = "EquipoSRE"
  }
}