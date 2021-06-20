#!/bin/bash

kubectl delete -f env.yml

kubectl delete -f  aws-pvc.yml 

kubectl delete -f namespace.yml

kubectl delete -f efs-csi-driver.yml

kubectl delete -f efs-sa.yml


