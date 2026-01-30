# Kubernetes Deployment Guide

This guide will walk you through deploying your Python backend to a local Kubernetes cluster using k3d.

## Step 1: Install k3d

### Windows (using chocolatey)
```powershell
choco install k3d
```

### Windows (manual download)
```powershell
# Download and install k3d
curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash
```

### Verify Installation
```bash
k3d version
kubectl version --client
```

## Step 2: Create k3d Cluster

```bash
# Create a cluster named "dev" with port mapping
k3d cluster create dev --port "8080:80@loadbalancer" --port "8000:8000@loadbalancer"

# Verify cluster is running
kubectl cluster-info
kubectl get nodes
```

## Step 3: Load Your Docker Image into k3d

```bash
# Build your image (if not already built)
docker build -t python-backend:latest .

# Load image into k3d cluster
k3d image import python-backend:latest --cluster dev
```

## Step 4: Deploy to Kubernetes

```bash
# Deploy the application
kubectl apply -f k8s-deployment.yaml

# Deploy the service
kubectl apply -f k8s-service.yaml

# Check if everything is running
kubectl get pods
kubectl get services
```

## Step 5: Access Your Application

```bash
# Get service details
kubectl get svc python-backend-service

# If using LoadBalancer type, access via:
# http://localhost:8000

# Alternative: Port forward
kubectl port-forward service/python-backend-service 8000:8000
```

## Useful Commands

```bash
# Check pod status and logs
kubectl get pods
kubectl logs <pod-name>
kubectl describe pod <pod-name>

# Check service
kubectl get services
kubectl describe service python-backend-service

# Delete resources
kubectl delete -f k8s-deployment.yaml
kubectl delete -f k8s-service.yaml

# Delete cluster
k3d cluster delete dev
```

## Understanding the YAML Files

### Deployment (k8s-deployment.yaml)
- **Deployment**: Manages your application pods
- **Replicas**: Number of pod copies (2 for high availability)
- **Container**: Your Python backend image
- **Health Checks**: Kubernetes monitors /health endpoint
- **Resources**: CPU and memory limits

### Service (k8s-service.yaml)
- **Service**: Network access to your pods
- **LoadBalancer**: Exposes service externally
- **Selector**: Routes traffic to pods with matching labels
- **Ports**: Maps external port to container port