# rwev [gitlab](https://rwev.gitlab.io) [github](https://rwev.github.io)
## development
### installation
```shell
python -m pip install -r requirements.txt
apt-get install entr
git clone --recursive https://github.com/getpelican/pelican-plugins
```
### generate site and serve on file change
```shell
fd '.*\.(py|html|md|less)$' | entr -r invoke rebuild serve
```
### gitlab user site 
a gitlab continuous integration file (`.gitlab-ci.yml`) is included in the repo. pushing to a user site repo (`<user>.gitlab.io`) run the build and deployment process.

### github user site 
using `ghp-import`: create branch `gh-pages` where `public` directory is root with command
```shell
ghp-import ./public -b gh-pages 
```
and push `gh-pages` branch to repository.
```shell
git push https://github.com/rwev/rwev.github.io.git gh-pages:gh-pages --force
```



export COUNT=0; for f in *.jpg
do { 
mv -- img_8133.jpg 16.jpg
export COUNT=17
} done
