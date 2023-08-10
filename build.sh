#!/bin/bash

set -e

if [[ "$1" = "-h" ]]; then
    echo "Usage: ./build.sh [BRANCH] [VERSION]..."
    exit 1
fi

branches=${1:-rawhide f38 f37 epel9}

if [[ $# -lt 2 ]]; then
    versions=('' 8.10 9.0 9.2 9.4 9.6)
else
    shift
    versions=("$@")
fi

if [[ -z "$ARCHOPT" ]]; then
    ARCHOPT=("-X ppc64le -R")
fi

for br in $branches; do
#    for arch in "-a x86_64" "-X x86_64 -R"; do
#    for arch in "-R"; do
        for ghc in "${versions[@]}"; do
          if [ "$br" != "f37" -a "$br" != "epel9" -o "$ghc" != "8.10" ]; then
            echo
            if [[ -z "$ghc" ]] && grep -q '^%global ghc_name' haskell-language-server.spec; then
                sed -i -e 's/%global ghc_name .*/#%%global ghc_name ghc9.4/' haskell-language-server.spec
            else
                sed -i -e 's/#%%global ghc_name/%global ghc_name/' -e s/'\(%global ghc_name ghc\).*'/'\1'"$ghc"/ haskell-language-server.spec
            fi
            ghc_name=$(grep '%global ghc_name' haskell-language-server.spec)
            echo "$ghc_name"
            if [ "$ghc_name" = "%global ghc_name ghc" ]; then
                echo "Illegal ghc_name!"
                exit 1
            else
                fbrnch copr haskell-language-server $br $ARCHOPT
            fi
          fi
        done
done
