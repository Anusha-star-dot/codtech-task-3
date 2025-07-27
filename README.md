\# CODTECH Task 3 - Microservices Kubernetes Deployment



This project demonstrates the deployment of a microservices-based application using Kubernetes.



\## 🔧 Structure



\- `backend/`: Backend service code and Dockerfile

\- `frontend/`: Frontend service placeholder

\- `k8s/`: Kubernetes deployment and service YAML files



\## 🚀 CI/CD



CI/CD is automated using \*\*GitHub Actions\*\*:

\- Docker build and push to Docker Hub

\- Kubernetes deployment using `kubectl`



\## 🐳 Docker Hub



Images are pushed to:  

📦 `docker.io/anushaice/backend:v1`



\## 🧪 How to Deploy



```bash

kubectl apply -f k8s/

kubectl get pods

kubectl port-forward svc/backend-service 5000:80

## 👩‍💻 Author

**Anusha Manikonda**  
DevOps Engineer | Kubernetes | Docker | Azure | AWS  
📧 anusm170@gmail.com  
🔗 [GitHub](https://github.com/Anusha-star-dot) | [LinkedIn](https://linkedin.com/in/anusha-manikonda-33331993)



