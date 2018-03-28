# コンテナのビルド(postgres)
cd postgres
docker build -t kube-postgres:1.0 .
# デプロイ(postgres)
kubectl create -f postgres-deployment.yml
kubectl create -f postgres-service.yml
# コンテナのビルド(python)
cd python
docker build -t kube-python:1.0 .
# デプロイ(python)
kubectl create -f python-deployment.yml
kubectl create -f python-service.yml
kubectl describe svc webapp-svc
# 実行
curl http://localhost:30080
