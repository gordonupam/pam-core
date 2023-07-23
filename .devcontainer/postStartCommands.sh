#!/bin/bash

conan user -r fitss > user.txt
grep '(anonymous)' user.txt 
if [ "$?" == "0" ]; then
  echo
  echo "** Conan fitss user is missing **"
  echo "Run the following command to add your user:"
  echo "  conan user -p -r fitss [name]"
else
  echo Conan Fitss User:
  conan user -r fitss
  echo
  echo Fitss Paackages:
  conan search -r fitss
fi
rm user.txt

