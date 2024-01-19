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
          if ! [ "$br" = "epel9" -a -z "$ghc" ]; then
            echo
            if [[ -z "$ghc" ]]; then
                if grep -q '^%global ghc_major' haskell-language-server.spec; then
                    sed -i -e 's/%global ghc_major .*/#%%global ghc_major 9.4/' haskell-language-server.spec
                fi
            else
                sed -i -e 's/#%%global ghc_major/%global ghc_major/' -e s/'\(%global ghc_major \).*'/'\1'"$ghc"/ haskell-language-server.spec
            fi
            case $ghc in
                9.8) LATEST=9.8.1 ;;
                9.6) LATEST=9.6.4 ;;
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
            ghc_major=$(grep '%global ghc_major' haskell-language-server.spec)
            case "$ghc_major" in
                "#%%global ghc_major "*) ;;
                *) echo "$ghc_major" ;;
            esac
            if [ "$ghc_major" = "%global ghc_major " ]; then
                echo "Illegal ghc_major!"
                exit 1
            else
                fbrnch copr haskell-language-server $br $ARCHOPT
            fi
          fi
        done
done
