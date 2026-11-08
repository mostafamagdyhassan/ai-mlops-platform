
# AWS Infrastructure

Terraform manages the AWS infrastructure for the AI MLOps Platform.

## Resources

- VPC
- Public and private subnets
- Internet Gateway
- NAT Gateway
- Route tables
- Amazon EKS
- EKS managed node groups
- IAM roles

## Region

Bahrain: me-south-1

## Prerequisites

- AWS CLI
- Terraform
- AWS credentials
- S3 Terraform state bucket
- State locking infrastructure

## Deployment

Initialize:

```bash
terraform init
```

Validate:

```bash
terraform fmt -recursive
terraform validate
```

Preview:

```bash
terraform plan -var-file=terraform.tfvars
```

Deploy:

```bash
terraform apply -var-file=terraform.tfvars
```

Destroy development infrastructure:

```bash
terraform destroy -var-file=terraform.tfvars
```

Always review the Terraform plan before applying changes.
Never commit Terraform state, credentials, or real tfvars files.
