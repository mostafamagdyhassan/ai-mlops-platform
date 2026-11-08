
provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = "AI-MLOps-Platform"
      Environment = var.environment
      ManagedBy   = "Terraform"
    }
  }
}
