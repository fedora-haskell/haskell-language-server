#!/bin/bash

set -e +x

if [[ "$1" = "-h" ]]; then
    echo "Usage: ./build.sh [BRANCH]..."
    exit 1
fi

branches=$*

if [[ -z "$ARCHOPT" ]]; then
    ARCHOPT=("-X ppc64le -R")
fi

for br in ${branches:-rawhide f39 f38 f37 epel9}; do
#    for arch in "-a x86_64" "-X x86_64 -R"; do
#    for arch in "-R"; do
    case $br in
        epel9) ghc="" ;;
        f37) ghc="" ;;
        *) ghc="8.10" ;;
    esac
    echo
    if [[ -z "$ghc" ]] && grep -q '^%global ghc_name' haskell-language-server.spec; then
        sed -i -e 's/%global ghc_name .*/#%%global ghc_name ghc8.10/' haskell-language-server.spec
    else
        sed -i -e 's/#%%global ghc_name/%global ghc_name/' -e s/'\(%global ghc_name ghc\).*'/'\1'"$ghc"/ haskell-language-server.spec
    fi
    LATEST=8.10.7
    ghcversion=$(fdrq $br --qf "%{version}" --latest-limit 1 ghc$ghc)
    if [ "$ghcversion" != "$LATEST" ]; then
        echo "repo ghc$ghc-$ghcversion is not $LATEST"
        exit 1
    else
        echo "$ghcversion"
        sed -i -e "s/%global ghc_minor .*/%global ghc_minor $ghcversion/" haskell-language-server.spec
    fi
    ghc_name=$(grep '%global ghc_name' haskell-language-server.spec)
    echo "$ghc_name"
    if [ "$ghc_name" = "%global ghc_name ghc" ]; then
        echo "Illegal ghc_name!"
        exit 1
    else
        fbrnch copr haskell-language-server $br $ARCHOPT
    fi
done
