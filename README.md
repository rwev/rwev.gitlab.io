# delma

## Setup

```shell
python -m pip install pelican markdown invoke
apt-get install entr
```

## Development

### Generate site and serve on file change
```shell
fd '.*\.(py|html|md)$' | entr -r invoke rebuild serve
```

