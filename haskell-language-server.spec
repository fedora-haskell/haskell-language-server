# generated by cabal-rpm-2.1.0 --standalone
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global ghc_without_dynamic 1
%global ghc_without_shared 1
%undefine with_ghc_prof
%undefine with_haddock
%global without_prof 1
%global without_haddock 1
%global debug_package %{nil}

%global pkg_name haskell-language-server
%global pkgver %{pkg_name}-%{version}

Name:           %{pkg_name}
Version:        1.8.0.0
Release:        1%{?dist}
Summary:        LSP server for GHC

License:        ASL 2.0
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources
Source1:        cabal.project
Patch0:         haskell-language-server-1.7.0.0-prettyprinter-1.7.patch

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cryptohash-sha1-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-ghc-devel
BuildRequires:  ghc-ghc-boot-th-devel
BuildRequires:  ghc-ghc-paths-devel
#BuildRequires:  ghc-ghcide-devel
BuildRequires:  ghc-githash-devel
BuildRequires:  ghc-gitrev-devel
BuildRequires:  ghc-hashable-devel
#BuildRequires:  ghc-hie-bios-devel
#BuildRequires:  ghc-hiedb-devel
#BuildRequires:  ghc-hls-alternate-number-format-plugin-devel
#BuildRequires:  ghc-hls-brittany-plugin-devel
#BuildRequires:  ghc-hls-call-hierarchy-plugin-devel
#BuildRequires:  ghc-hls-change-type-signature-plugin-devel
#BuildRequires:  ghc-hls-class-plugin-devel
#BuildRequires:  ghc-hls-code-range-plugin-devel
#BuildRequires:  ghc-hls-eval-plugin-devel
#BuildRequires:  ghc-hls-explicit-fixity-plugin-devel
#BuildRequires:  ghc-hls-explicit-imports-plugin-devel
#BuildRequires:  ghc-hls-floskell-plugin-devel
#BuildRequires:  ghc-hls-fourmolu-plugin-devel
#BuildRequires:  ghc-hls-gadt-plugin-devel
#BuildRequires:  ghc-hls-graph-devel
#BuildRequires:  ghc-hls-haddock-comments-plugin-devel
#BuildRequires:  ghc-hls-hlint-plugin-devel
#BuildRequires:  ghc-hls-module-name-plugin-devel
#BuildRequires:  ghc-hls-ormolu-plugin-devel
#BuildRequires:  ghc-hls-plugin-api-devel
#BuildRequires:  ghc-hls-pragmas-plugin-devel
#BuildRequires:  ghc-hls-qualify-imported-names-plugin-devel
#BuildRequires:  ghc-hls-refactor-plugin-devel
#BuildRequires:  ghc-hls-refine-imports-plugin-devel
#BuildRequires:  ghc-hls-rename-plugin-devel
#BuildRequires:  ghc-hls-retrie-plugin-devel
#BuildRequires:  ghc-hls-splice-plugin-devel
#BuildRequires:  ghc-hls-stan-plugin-devel
#BuildRequires:  ghc-hls-stylish-haskell-plugin-devel
#BuildRequires:  ghc-hls-tactics-plugin-devel
BuildRequires:  ghc-hslogger-devel
BuildRequires:  ghc-lens-devel
#BuildRequires:  ghc-lsp-devel
#BuildRequires:  ghc-lsp-types-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-optparse-simple-devel
BuildRequires:  ghc-prettyprinter-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-safe-exceptions-devel
#BuildRequires:  ghc-sqlite-simple-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unliftio-core-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  cabal-install > 1.18
# for missing dep 'ghcide':
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-Glob-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-case-insensitive-devel
#BuildRequires:  ghc-co-log-core-devel
#BuildRequires:  ghc-dependent-map-devel
#BuildRequires:  ghc-dependent-sum-devel
BuildRequires:  ghc-dlist-devel
#BuildRequires:  ghc-enummapset-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-fingertree-devel
#BuildRequires:  ghc-focus-devel
BuildRequires:  ghc-ghc-boot-devel
#BuildRequires:  ghc-ghc-check-devel
#BuildRequires:  ghc-ghc-trace-events-devel
BuildRequires:  ghc-haddock-library-devel
#BuildRequires:  ghc-heapsize-devel
#BuildRequires:  ghc-hie-compat-devel
#BuildRequires:  ghc-implicit-hie-cradle-devel
#BuildRequires:  ghc-list-t-devel
BuildRequires:  ghc-monoid-subclasses-devel
#BuildRequires:  ghc-opentelemetry-devel
BuildRequires:  ghc-parallel-devel
BuildRequires:  ghc-prettyprinter-ansi-terminal-devel
BuildRequires:  ghc-random-devel
#BuildRequires:  ghc-sorted-list-devel
#BuildRequires:  ghc-stm-containers-devel
BuildRequires:  ghc-syb-devel
#BuildRequires:  ghc-text-rope-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unliftio-devel
BuildRequires:  ghc-vector-devel
# for missing dep 'hie-bios':
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-yaml-devel
# for missing dep 'hiedb':
#BuildRequires:  ghc-algebraic-graphs-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-array-devel
#BuildRequires:  ghc-hie-compat-devel
BuildRequires:  ghc-lucid-devel
BuildRequires:  ghc-terminal-size-devel
# for missing dep 'hls-alternate-number-format-plugin':
#BuildRequires:  ghc-hie-compat-devel
BuildRequires:  ghc-syb-devel
# for missing dep 'hls-brittany-plugin':
#BuildRequires:  ghc-brittany-devel
#BuildRequires:  ghc-czipwith-devel
#BuildRequires:  ghc-ghc-exactprint-devel
# for missing dep 'hls-change-type-signature-plugin':
BuildRequires:  ghc-syb-devel
# for missing dep 'hls-class-plugin':
#BuildRequires:  ghc-ghc-exactprint-devel
# for missing dep 'hls-code-range-plugin':
BuildRequires:  ghc-semigroupoids-devel
BuildRequires:  ghc-vector-devel
# for missing dep 'hls-eval-plugin':
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-parser-combinators-devel
BuildRequires:  ghc-pretty-simple-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unliftio-devel
# for missing dep 'hls-floskell-plugin':
#BuildRequires:  ghc-floskell-devel
# for missing dep 'hls-fourmolu-plugin':
#BuildRequires:  ghc-fourmolu-devel
#BuildRequires:  ghc-process-extras-devel
# for missing dep 'hls-gadt-plugin':
#BuildRequires:  ghc-ghc-exactprint-devel
# for missing dep 'hls-graph':
BuildRequires:  ghc-exceptions-devel
#BuildRequires:  ghc-focus-devel
BuildRequires:  ghc-js-dgtable-devel
BuildRequires:  ghc-js-flot-devel
BuildRequires:  ghc-js-jquery-devel
#BuildRequires:  ghc-list-t-devel
BuildRequires:  ghc-primitive-devel
#BuildRequires:  ghc-stm-containers-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unliftio-devel
# for missing dep 'hls-haddock-comments-plugin':
#BuildRequires:  ghc-ghc-exactprint-devel
# for missing dep 'hls-hlint-plugin':
BuildRequires:  ghc-Diff-devel
#BuildRequires:  ghc-apply-refact-devel
#BuildRequires:  ghc-ghc-exactprint-devel
BuildRequires:  ghc-ghc-lib-parser-devel
BuildRequires:  ghc-ghc-lib-parser-ex-devel
BuildRequires:  ghc-hlint-devel
BuildRequires:  ghc-refact-devel
# for missing dep 'hls-ormolu-plugin':
BuildRequires:  ghc-ormolu-devel
# for missing dep 'hls-plugin-api':
BuildRequires:  ghc-Diff-devel
#BuildRequires:  ghc-dependent-map-devel
#BuildRequires:  ghc-dependent-sum-devel
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-lens-aeson-devel
#BuildRequires:  ghc-opentelemetry-devel
# for missing dep 'hls-pragmas-plugin':
#BuildRequires:  ghc-fuzzy-devel
# for missing dep 'hls-qualify-imported-names-plugin':
BuildRequires:  ghc-dlist-devel
# for missing dep 'hls-refactor-plugin':
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-ghc-boot-devel
#BuildRequires:  ghc-ghc-exactprint-devel
#BuildRequires:  ghc-retrie-devel
BuildRequires:  ghc-syb-devel
#BuildRequires:  ghc-text-rope-devel
BuildRequires:  ghc-time-devel
# for missing dep 'hls-rename-plugin':
#BuildRequires:  ghc-ghc-exactprint-devel
#BuildRequires:  ghc-mod-devel
BuildRequires:  ghc-syb-devel
# for missing dep 'hls-retrie-plugin':
#BuildRequires:  ghc-retrie-devel
# for missing dep 'hls-splice-plugin':
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-foldl-devel
#BuildRequires:  ghc-ghc-exactprint-devel
#BuildRequires:  ghc-retrie-devel
BuildRequires:  ghc-syb-devel
# for missing dep 'hls-stan-plugin':
#BuildRequires:  ghc-stan-devel
# for missing dep 'hls-stylish-haskell-plugin':
#BuildRequires:  ghc-stylish-haskell-devel
# for missing dep 'hls-tactics-plugin':
BuildRequires:  ghc-fingertree-devel
#BuildRequires:  ghc-generic-lens-devel
#BuildRequires:  ghc-ghc-exactprint-devel
#BuildRequires:  ghc-ghc-source-gen-devel
#BuildRequires:  ghc-hyphenation-devel
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-parser-combinators-devel
#BuildRequires:  ghc-refinery-devel
#BuildRequires:  ghc-retrie-devel
BuildRequires:  ghc-syb-devel
#BuildRequires:  ghc-unagi-chan-devel
# for missing dep 'lsp':
BuildRequires:  ghc-attoparsec-devel
#BuildRequires:  ghc-dependent-map-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-scientific-devel
#BuildRequires:  ghc-sorted-list-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-uuid-devel
# for missing dep 'sqlite-simple':
BuildRequires:  ghc-Only-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-blaze-textual-devel
#BuildRequires:  ghc-direct-sqlite-devel
BuildRequires:  ghc-semigroups-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-time-devel
# for missing dep 'lsp-types':
#BuildRequires:  ghc-dependent-sum-devel
#BuildRequires:  ghc-dependent-sum-template-devel
BuildRequires:  ghc-network-uri-devel
#BuildRequires:  ghc-rope-utf16-splay-devel
BuildRequires:  ghc-scientific-devel
#BuildRequires:  ghc-some-devel
BuildRequires:  ghc-template-haskell-devel
# End cabal-rpm deps
# more missing subdeps
BuildRequires:  ghc-HsYAML-devel
BuildRequires:  ghc-MonadRandom-devel
BuildRequires:  ghc-constraints-devel
BuildRequires:  ghc-filemanip-devel
BuildRequires:  ghc-hashtables-devel
BuildRequires:  ghc-haskell-src-exts-devel
BuildRequires:  ghc-indexed-profunctors-devel
BuildRequires:  ghc-logict-devel
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-microlens-th-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-psqueues-devel
BuildRequires:  ghc-type-equality-devel

%if %{defined ghc_version}
Recommends: ghc = %{ghc_version}
%endif
Recommends: cabal-install
#Recommends: stack

%description
The official Haskell language server (LSP) implementation.

Please see the README on GitHub at
<https://github.com/haskell/haskell-language-server#readme>.


%prep
# Begin cabal-rpm setup:
%autosetup -p1
# End cabal-rpm setup
cabal-tweak-flag dynamic False
%if %{undefined ghc_name}
cabal-tweak-flag hlint False
%endif
cabal unpack hls-qualify-imported-names-plugin-1.0.1.0
(
cd hls-qualify-imported-names-plugin-1.0.1.0
sed -i -e 's/=1.4/=1.5/' -e 's/=1.7/=1.8/' hls-qualify-imported-names-plugin.cabal
)
cabal unpack hls-stylish-haskell-plugin-1.0.1.1
(
cd hls-stylish-haskell-plugin-1.0.1.1
sed -i -e 's/=1.4/=1.5/' -e 's/=1.7/=1.8/' hls-stylish-haskell-plugin.cabal
)
cp -p %{SOURCE1} .


%build
# Begin cabal-rpm build:
cabal update
# End cabal-rpm build


%install
# Begin cabal-rpm install
mkdir -p %{buildroot}%{_bindir}
%if 0%{?fedora} >= 36
%ghc_set_gcc_flags
%endif
cabal install --install-method=copy --enable-executable-stripping --installdir=%{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
%{buildroot}%{_bindir}/%{name} --bash-completion-script %{name} | sed s/filenames/default/ > %{buildroot}%{_datadir}/bash-completion/completions/%{name}
%{buildroot}%{_bindir}/haskell-language-server-wrapper --bash-completion-script haskell-language-server-wrapper | sed s/filenames/default/ > %{buildroot}%{_datadir}/bash-completion/completions/haskell-language-server-wrapper
# End cabal-rpm install


%files
# Begin cabal-rpm files:
%license LICENSE
%doc ChangeLog.md README.md
%{_bindir}/%{name}
%{_bindir}/haskell-language-server-wrapper
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/bash-completion/completions/haskell-language-server-wrapper
# End cabal-rpm files


%changelog
* Sun Sep 18 2022 Jens Petersen <petersen@redhat.com> - 1.8.0.0-1
- https://hackage.haskell.org/package/haskell-language-server-1.8.0.0/changelog

* Thu Apr 28 2022 Jens Petersen <petersen@redhat.com> - 1.7.0.0-1
- https://hackage.haskell.org/package/haskell-language-server-1.7.0.0/changelog

* Mon Jan 31 2022 Jens Petersen <petersen@redhat.com> - 1.6.1.0-1
- https://hackage.haskell.org/package/haskell-language-server-1.6.1.0/changelog
- disable dynamic linking

* Tue Nov 30 2021 Jens Petersen <petersen@redhat.com> - 1.5.1.0-1
- https://hackage.haskell.org/package/haskell-language-server-1.5.1.0/changelog

* Wed Oct 13 2021 Jens Petersen <petersen@redhat.com> - 1.4.0.0-1
- initial packaging
