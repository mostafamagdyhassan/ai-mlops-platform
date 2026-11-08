
# DevSecOps

Security is integrated throughout the development lifecycle.

## Tools

- Trivy: Container, filesystem and dependency scanning.
- Checkov: Terraform security analysis.
- SonarQube: Code quality and security analysis.
- Kubernetes Pod Security Standards.
- IAM and Kubernetes RBAC.
- Image signing and supply-chain verification.

## Security principles

- Least privilege.
- Non-root containers.
- No hardcoded credentials.
- Encrypted storage.
- Private networking.
- Image vulnerability scanning.
- Infrastructure policy validation.
- Human approval for sensitive remediation actions.

## Run Trivy

```bash
trivy fs --config security/trivy/trivy.yaml .
```

## Run Checkov

```bash
checkov -d infrastructure/terraform \
  --config-file security/checkov/checkov.yaml
```
