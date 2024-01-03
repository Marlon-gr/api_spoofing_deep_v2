#!/bin/sh
set -euo pipefail

##############################################
# Shell tests to run before the image is build
#
# See the README.md file for running instructions
##############################################

SCRIPT_NAME=$(basename "$0")

echo ''
echo "[$SCRIPT_NAME] >> Starting pre-build tests ..."

# TODO adicione os seus testes aqui

echo "[$SCRIPT_NAME] >> Finished pre-build tests."
echo ''
