# scaleway-registery-bug-reproduce

Steps:

* Create a Scaleway registry namespace (rg.fr-par.scw.cloud/namespace-nice-nightingale for my tests)
* Create API key with ContainerRegistryFullAccess to the project
* Start fresh debian VM (tested with scaleway instance DEV1-S in PARIS-2 with Debian Bookworm)
* Install docker :
```
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

* Install scw cli:
```curl -s https://raw.githubusercontent.com/scaleway/scaleway-cli/master/scripts/get.sh | sh```

* Install API key
```scw init -p newprofile  access-key=```

* Login to Docker with scw
```scw registry login -p newprofile```

* Clone repository
```git clone https://github.com/akimed/scaleway-registery-bug-reproduce.git && cd scaleway-registery-bug-reproduce```

Change the registry namespace in compose.yml and compose.local.yml

* Build, then push, then build, then push, then build, then push
```sudo docker compose -f compose.yml -f compose.local.yml build --no-cache
sudo docker compose -f compose.yml -f compose.local.yml push
```

You might need to repeat it a few time (build then push) to obtain the following:

```received unexpected HTTP status: 500```
