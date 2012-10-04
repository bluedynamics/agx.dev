python2.6 --version
virtualenv env
python bootstrap.py -c dev.cfg
bin/buildout -c dev.cfg
./test.sh