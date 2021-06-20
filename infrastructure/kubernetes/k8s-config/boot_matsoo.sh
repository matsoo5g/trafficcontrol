#!/bin/bash

kubectl create -f namespace.yml

kubectl create -f efs-csi-driver.yml

kubectl create -f efs-sa.yml

# wait a moment for efs pvc bounding success
sleep 5 

kubectl create -f aws-pvc.yml 

kubectl create -f env.yml
