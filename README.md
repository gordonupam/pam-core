# Pam-core Conan Packaging

0.1.  > git submodule add ssh://git@git.pyrsoftware.ca:2222/ser/protocols.git src/protocols
      > git submodule add ssh://git@git.pyrsoftware.ca:2222/ser/coreserver.git src/coreserver
      > git submodule add ssh://git@git.pyrsoftware.ca:2222/ser/pyr-shared.git src/pyr-shared

## How to build

1. Make an out-of-source build directory.

```
mkdir build
cd build
```

2. Tell Conan to install our dependencies for a Debug build, and build any that need to be built.

    conan install .. -s build_type=Debug --build=missing -o pokerstars-commlib:USE_STANDARD_OPENSSL=True -o pokerstars-commlib:USE_OPENSSL3=True

3. Configure the build using CMake.

    cmake .. -DCMAKE_BUILD_TYPE=Debug
    
    For Windows, you may need to add  '-DCMAKE_GENERATOR_TOOLSET=v141'
    

4. To create package:

    conan create .. -s build_type=Debug -o pokerstars-commlib:USE_STANDARD_OPENSSL=True  -o pokerstars-commlib:USE_OPENSSL3=True

5. Upload the package.


conan upload -r fitss --all pam-core/*


