# CI/CD Pipeline Setup Guide

This guide will help you set up a complete CI/CD pipeline using GitHub Actions.

## 🚀 Quick Setup Steps

### 1. Create Docker Hub Account
- Go to https://hub.docker.com
- Create a free account
- Create a repository: `your-username/python-backend`

### 2. Generate Docker Hub Access Token
- Go to Docker Hub → Account Settings → Security
- Click "New Access Token"
- Name: `github-actions`
- Copy the token (you'll need it for GitHub secrets)

### 3. Update Workflow Configuration
Edit `.github/workflows/ci-cd.yml` and replace:
```yaml
env:
  DOCKER_IMAGE_NAME: your-dockerhub-username/python-backend  # ← Change this!
```

### 4. Create GitHub Repository
```bash
# Initialize git repository
git init
git add .
git commit -m "Initial commit: Python backend with CI/CD"

# Create GitHub repository (on GitHub.com)
# Then connect your local repo:
git remote add origin https://github.com/your-username/python-backend.git
git branch -M main
git push -u origin main
```

### 5. Add GitHub Secrets
Go to your GitHub repository → Settings → Secrets and variables → Actions

Add these Repository Secrets:
- `DOCKERHUB_USERNAME`: Your Docker Hub username
- `DOCKERHUB_TOKEN`: The access token you generated

## 🔄 How the Pipeline Works

### Trigger: Push to main branch
```
Push code → GitHub Actions starts automatically
```

### Stage 1: Test 🧪
```
✅ Checkout code
✅ Setup Python 3.11
✅ Install dependencies
✅ Run FastAPI server
✅ Test /health endpoint
✅ Test /items endpoint
```

### Stage 2: Build & Push 🏗️
```
✅ Checkout code
✅ Setup Docker Buildx
✅ Login to Docker Hub
✅ Build Docker image
✅ Tag with 'latest' and git commit SHA
✅ Push to Docker Hub
```

### Stage 3: Deploy 🚀 (Bonus)
```
✅ Checkout code
✅ Setup kubectl and k3d
✅ Create k3d cluster
✅ Update deployment with new image
✅ Deploy to Kubernetes
✅ Verify deployment works
```

## 🎯 What You Get

### Automatic Testing
Every code push runs tests to ensure your API works

### Automatic Building
Every successful test triggers a Docker build and push

### Automatic Deployment
Every successful build deploys to a fresh k3d cluster

### Version Tracking
Each build is tagged with the git commit SHA for traceability

### Rollback Capability
You can easily rollback to any previous version using the git SHA tags

## 🔧 Local Testing

Test the workflow locally before pushing:

```bash
# Test the app
python -m uvicorn main:app --reload

# Test Docker build
docker build -t test-backend .
docker run -p 8000:8000 test-backend

# Test Kubernetes deployment
kubectl apply -f k8s-deployment.yaml
kubectl apply -f k8s-service.yaml
```

## 📊 Monitoring Your Pipeline

- **GitHub Actions tab**: See workflow runs and logs
- **Docker Hub**: See your built images
- **kubectl commands**: Monitor deployments

```bash
# Check workflow status
git push origin main
# → Visit GitHub.com → Your repo → Actions tab

# Check Docker Hub
# → Visit hub.docker.com → Your repository

# Check deployment (if using local k3d)
kubectl get pods
kubectl logs -l app=python-backend
```