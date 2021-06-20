## Kubernetes CDN deployment

You will deploy whole CDN services by the kubeconfig files under this directory.
Please follow the proceduces as below.

### Deployment

1. Build the images
need to build RPMs and docker images by docker-compose file

```
// build RPMs, only need to build once, no need to build everytime if there is not code pushed 
$ make

// build docker images
$ docker-compose build

```

2. Push images to AWS ECR

 
- Modify the script `push_cdn_to_registry.sh` and run it

```
$ ./push_cdn_to_registry.sh
```

3. Setup `kubectl` accessing permission

```
$ aws eks update-kubeconfig --region $REGION --name $EKS_CLUSTER_NAME
```

4. Run Matsoo's environment setup

```
$ ./k8s-conf/boot_matsoo.sh
```

5. Run computing components

```
//create the containers which required to be ready first, e.g. databases 
$ kubectl create -f k8s-config/nodes/db-enroller-smtp.yml
//wait few seconds then create the other nodes
$ kubectl create -f k8s-config/nodes/other-components.yml
```

Optional: you can then create cache servers for verifying the functionality of CDN. 
These cache servers would not run at Wavelength, since EKS current not support to have this integration.

```
$ kubectl create -f k8s-config/nodes/cache-servers.yml
``` 

6. Clean everything

- Remove your computing nodes first

```
$ kubectl create -f k8s-config/nodes/
```

- Removing other environment setup

```
$ ./rm_matsoo.sh
```
