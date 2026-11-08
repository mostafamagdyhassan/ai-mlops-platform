
# Kubernetes Deployment

This directory contains Kubernetes resources for the AI MLOps platform.

## Resources

- Application namespace
- Resource quotas
- API deployment
- ML model deployment
- Kubernetes services
- Network policies
- Security contexts
- Health probes

## Deploy

```bash
kubectl apply -f kubernetes/namespaces/
kubectl apply -f kubernetes/deployments/
kubectl apply -f kubernetes/policies/
```

Check deployments:

```bash
kubectl get deployments -n ai-platform
kubectl get pods -n ai-platform
kubectl get services -n ai-platform
```

The API requires a Kubernetes Secret named `aiops-secrets` containing `database-url` before deployment.

Network policies must be reviewed against the cluster's network plugin and the actual service communication requirements.
