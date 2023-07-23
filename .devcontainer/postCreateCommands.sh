#!/bin/bash

conan profile new default --detect && conan profile update settings.compiler.libcxx=libstdc++11 default
conan remote add --insert 0 fitss https://artifactory.pyrsoftware.ca/artifactory/api/conan/fitss-conan

