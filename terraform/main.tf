terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "eu-west-2"
}

resource "aws_vpc" "ot_gateway" {
  cidr_block           = "10.20.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "ot-gateway-vpc"
  }
}

resource "aws_subnet" "ot_dmz" {
  vpc_id                  = aws_vpc.ot_gateway.id
  cidr_block              = "10.20.1.0/24"
  map_public_ip_on_launch = false

  tags = {
    Name = "ot-gateway-dmz"
  }
}
