python --version
virtualenv env
env/bin/python bootstrap.py -c dev.cfg
bin/buildout -c dev.cfg
./test.sh
