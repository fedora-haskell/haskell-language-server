#!/bin/bash

set -e +x

if [[ "$1" = "-h" ]]; then
    echo "Usage: ./build.sh [BRANCH] [VERSION]..."
    exit 1
fi

branches=${1:-rawhide f39 f38 epel9}

if [[ $# -lt 2 ]]; then
    versions=('' 9.6 9.4 9.2)
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
            case $ghc in
                9.8) LATEST=9.8.1 ;;
                9.6) LATEST=9.6.3 ;;
                9.4) LATEST=9.4.8 ;;
                9.2) LATEST=9.2.8 ;;
                9.0) LATEST=9.0.2 ;;
                8.10) LATEST=8.10.7 ;;
                '') ;;
                *) echo "unknown major version: $ghc"
                   exit 1
                   ;;
            esac
            ghcversion=$(fdrq $br --qf "%{version}" --latest-limit 1 ghc$ghc)
            if [ -n "$LATEST" -a "$ghcversion" != "$LATEST" ]; then
                echo "repo ghc$ghc-$ghcversion /= $LATEST"
            fi
            echo "$ghcversion"
            sed -i -e "s/%global ghc_minor .*/%global ghc_minor $ghcversion/" haskell-language-server.spec
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
