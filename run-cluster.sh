#!/bin/bash

kind create cluster --name mini-gitops

helm install demo-service charts/demo-service -f charts/demo-service/values.yaml

kubectl port-forward service/demo-service-service 8000:80
