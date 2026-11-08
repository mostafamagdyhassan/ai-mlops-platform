
terraform {
  required_version = ">= 1.8.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket         = "REPLACE_WITH_TERRAFORM_STATE_BUCKET"
    key            = "ai-mlops-platform/terraform.tfstate"
    region         = "me-south-1"
    dynamodb_table = "REPLACE_WITH_STATE_LOCK_TABLE"
    encrypt        = true
  }
}
