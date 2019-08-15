# delma

## Setup

```shell
python -m pip install -r requirements.txt
apt-get install entr
```

## Development

### Generate site and serve on file change
```shell
fd '.*\.(py|html|md|css|less)$' | entr -r invoke rebuild serve
```

### Push to GitLab/Hub user site repository
Create branch `ghl-pages` called where `output` directory is root
```shell
ghp-import ./output -b ghl-pages 
```
Push `ghl-pages` branch to repository.
```shell
git push https://github.com/rwev/rwev.github.io.git ghl-pages:master --force
git push https://gitlab.com/rwev/rwev.gitlab.io.git ghl-pages:master --force
```



