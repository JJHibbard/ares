export ARES=$TRAVIS_BUILD_DIR    
python setup.py install
python remote.py minimal
echo "backend : Agg" > $HOME/matplotlibrc
export MATPLOTLIBRC=$HOME
./run_tests.sh

