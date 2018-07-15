# Give it an AlphaTwirl

Example code for making use of AlphaTwirl

# Download and setup

```
git clone --recursive git@github.com:alphatwirl/give-it-an-alphatwirl.git
cd give-it-an-alphatwirl
cd <example you are interested in>
```

# On non-scientific linux 6 machines

E.g. on OS X/other Linux/Windows

1. Install [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
2. Install [Vagrant](https://www.vagrantup.com/downloads.html)
    - You might need to also install `vagrant-libvirt` on some systems if you see "The provider 'libvirt' could not be found, but was requested to back the machine 'default'. Please use a provider that exists."

1. run

  ```bash
  git clone --recursive git@github.com:alphatwirl/give-it-an-alphatwirl.git
  cd give-it-an-alphatwirl
  vagrant up # wait
  vagrant ssh
  cd /vagrant
  cd <example you are interested in>
  ```

# With Docker
```
# pip install --user docker-compose
docker-compose up -d
docker exec -ti  giveitanalphatwirl_analysis-box_1 cdw
cd <example you are interested in>
python run.py
```

# Using the examples

(To be written)
