cd ./build_files
ls
rm *.rst
ls
sphinx-apidoc -o build_files ../riid
sphinx-build -b html ./build_files ./