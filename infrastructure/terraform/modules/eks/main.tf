
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"

  cluster_name    = "${var.project_name}-${var.environment}"
  cluster_version = var.cluster_version

  cluster_endpoint_public_access = true

  cluster_endpoint_public_access_cidrs = ["REPLACE_WITH_YOUR_PUBLIC_IP/32"]

  enable_cluster_creator_admin_permissions = true

  vpc_id     = data.aws_subnet.selected.vpc_id
  subnet_ids = var.subnet_ids

  eks_managed_node_groups = {
    general = {
      instance_types = [var.node_instance_type]

      min_size     = var.min_nodes
      max_size     = var.max_nodes
      desired_size = var.desired_nodes

      labels = {
        role = "general"
      }
    }
  }

  tags = {
    Project     = var.project_name
    Environment = var.environment
  }
}

data "aws_subnet" "selected" {
  id = var.subnet_ids[0]
}

output "cluster_name" {
  value = module.eks.cluster_name
}

output "cluster_endpoint" {
  value = module.eks.cluster_endpoint
}
