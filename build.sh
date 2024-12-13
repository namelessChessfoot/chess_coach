pip3 install -r requirements.txt

src="./engines_src"
bin="./engines"

rm -rf $src
rm -rf $bin
mkdir $src
mkdir $bin

cd $src
    git clone git@github.com:official-stockfish/Stockfish.git
    cd ./Stockfish/src
        make -j profile-build
        mv ./stockfish ../../../$bin
    cd ../../
cd ..

