# [gitlab user page](https://rwev.gitlab.io) 
## development
### installation
```shell
python -m pip install -r requirements.txt
apt-get install entr
git clone --recursive https://github.com/getpelican/pelican-plugins
```
### generate site and serve on file change
```shell
fd '.*\.(py|html|md|less|css|js)$' | entr -r invoke rebuild serve
```
### deployment
a gitlab continuous integration file (`.gitlab-ci.yml`) is included in the repo. pushing to a user site repo (`<user>.gitlab.io`) run the build and deployment process.


export COUNT=0; for f in *.jpg
do { 
mv -- img_8133.jpg 16.jpg
export COUNT=17
} done
