# delma

## Setup

```shell
python -m pip install pelican markdown
apt-get install entr
```

## Development

### Generate site on file change
```shell
fd --full-path ./ | entr pelican content -t ./theme -s pelicanconf.py
```

### Restart server on file change
```shell
fd --full-path ./ | entr -r pelican --listen
```
