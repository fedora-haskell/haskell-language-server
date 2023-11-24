# generated by cabal-rpm-2.1.5 --standalone --stream hackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

#%%global ghc_name ghc9.4
%global ghc_minor 9.4.5
%if 0%{?fedora} > 37
%bcond_with compiler_default
%else
# ghc_version macro needs /usr/bin/ghc
%bcond_without compiler_default
%endif

%global ghc_prefix %{?ghc_name}%{!?ghc_name:ghc}

%global wrapper_pkg 0%{?fedora} < 38 && "%{?ghc_name}" == "ghc9.2" || 0%{?fedora} >= 38 &&  "%{?ghc_name}" == ""

%global ghc_without_dynamic 1
%global ghc_without_shared 1
%undefine with_ghc_prof
%undefine with_haddock
%global without_prof 1
%global without_haddock 1
%global debug_package %{nil}

%global pkg_name haskell-language-server
%global pkgver %{pkg_name}-%{version}

%global executable %{pkg_name}-%{ghc_version}

Name:           %{pkg_name}%{?ghc_name:-%{ghc_name}}
Version:        2.4.0.0
Release:        4%{?dist}.ghc%{ghc_minor}
Summary:        LSP server for GHC %{ghc_version}

License:        Apache-2.0
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources
Provides:       haskell-language-server-ghc-%{ghc_version} = %{version}-%{release}

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
%if %{defined ghc_name}
BuildRequires:  %{ghc_name} = %{ghc_minor}
%if %{with compiler_default}
BuildRequires:  %{ghc_name}-compiler-default = %{ghc_minor}
%endif
BuildRequires:  zlib-devel
%else
BuildRequires:  ghc-compiler = %{ghc_minor}
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
%if %{defined fedora}
BuildRequires:  ghc-cryptohash-sha1-devel
%endif
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-ghc-devel
BuildRequires:  ghc-ghc-boot-th-devel
BuildRequires:  ghc-ghc-paths-devel
#BuildRequires:  ghc-ghcide-devel
%if %{defined fedora}
BuildRequires:  ghc-githash-devel
%endif
BuildRequires:  ghc-gitrev-devel
BuildRequires:  ghc-hashable-devel
#BuildRequires:  ghc-hie-bios-devel
#BuildRequires:  ghc-hiedb-devel
#BuildRequires:  ghc-hls-alternate-number-format-plugin-devel
#BuildRequires:  ghc-hls-cabal-fmt-plugin-devel
#BuildRequires:  ghc-hls-cabal-plugin-devel
#BuildRequires:  ghc-hls-call-hierarchy-plugin-devel
#BuildRequires:  ghc-hls-change-type-signature-plugin-devel
#BuildRequires:  ghc-hls-class-plugin-devel
#BuildRequires:  ghc-hls-code-range-plugin-devel
#BuildRequires:  ghc-hls-eval-plugin-devel
#BuildRequires:  ghc-hls-explicit-fixity-plugin-devel
#BuildRequires:  ghc-hls-explicit-imports-plugin-devel
#BuildRequires:  ghc-hls-explicit-record-fields-plugin-devel
#BuildRequires:  ghc-hls-floskell-plugin-devel
#BuildRequires:  ghc-hls-fourmolu-plugin-devel
#BuildRequires:  ghc-hls-gadt-plugin-devel
#BuildRequires:  ghc-hls-graph-devel
#BuildRequires:  ghc-hls-hlint-plugin-devel
#BuildRequires:  ghc-hls-module-name-plugin-devel
#BuildRequires:  ghc-hls-ormolu-plugin-devel
#BuildRequires:  ghc-hls-overloaded-record-dot-plugin-devel
#BuildRequires:  ghc-hls-plugin-api-devel
#BuildRequires:  ghc-hls-pragmas-plugin-devel
#BuildRequires:  ghc-hls-qualify-imported-names-plugin-devel
#BuildRequires:  ghc-hls-refactor-plugin-devel
#BuildRequires:  ghc-hls-rename-plugin-devel
#BuildRequires:  ghc-hls-retrie-plugin-devel
#BuildRequires:  ghc-hls-splice-plugin-devel
#BuildRequires:  ghc-hls-stylish-haskell-plugin-devel
%if %{defined fedora}
BuildRequires:  ghc-lens-devel
%endif
#BuildRequires:  ghc-lsp-devel
#BuildRequires:  ghc-lsp-types-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-optparse-applicative-devel
%if %{defined fedora}
BuildRequires:  ghc-optparse-simple-devel
BuildRequires:  ghc-prettyprinter-devel
%endif
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-regex-tdfa-devel
%if %{defined fedora}
BuildRequires:  ghc-safe-exceptions-devel
%endif
#BuildRequires:  ghc-sqlite-simple-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
%if %{defined fedora}
BuildRequires:  ghc-unliftio-core-devel
%endif
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  cabal-install > 1.18
# for missing dep 'HsYAML-aeson':
BuildRequires:  ghc-HsYAML-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-vector-devel
# for missing dep 'ListLike':
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-vector-devel
# for missing dep 'algebraic-graphs':
BuildRequires:  ghc-array-devel
# for missing dep 'apply-refact':
BuildRequires:  ghc-filemanip-devel
BuildRequires:  ghc-refact-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-uniplate-devel
BuildRequires:  ghc-unix-compat-devel
# for missing dep 'attoparsec-aeson':
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-vector-devel
# for missing dep 'constraints-extras':
BuildRequires:  ghc-constraints-devel
BuildRequires:  ghc-template-haskell-devel
# for missing dep 'dependent-sum':
BuildRequires:  ghc-some-devel
# for missing dep 'floskell':
BuildRequires:  ghc-ansi-wl-pprint-devel
BuildRequires:  ghc-attoparsec-devel
%if %{defined fedora}
BuildRequires:  ghc-haskell-src-exts-devel
%endif
# for missing dep 'fourmolu':
BuildRequires:  ghc-Cabal-syntax-devel
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-MemoTrie-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-ghc-lib-parser-devel
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-th-env-devel
BuildRequires:  ghc-yaml-devel
# for missing dep 'fuzzy':
BuildRequires:  ghc-monoid-subclasses-devel
# for missing dep 'generic-lens':
BuildRequires:  ghc-profunctors-devel
# for missing dep 'ghc-check':
BuildRequires:  ghc-ghc-boot-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-th-compat-devel
# for missing dep 'ghcide':
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-Glob-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-exceptions-devel
%if %{defined fedora}
BuildRequires:  ghc-fingertree-devel
%endif
BuildRequires:  ghc-ghc-boot-devel
BuildRequires:  ghc-haddock-library-devel
BuildRequires:  ghc-parallel-devel
%if %{defined fedora}
BuildRequires:  ghc-prettyprinter-ansi-terminal-devel
%endif
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-time-devel
%if %{defined fedora}
BuildRequires:  ghc-unliftio-devel
%endif
BuildRequires:  ghc-vector-devel
# for missing dep 'hie-bios':
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-yaml-devel
# for missing dep 'hie-compat':
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-ghc-boot-devel
# for missing dep 'hiedb':
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-array-devel
%if %{defined fedora}
BuildRequires:  ghc-lucid-devel
BuildRequires:  ghc-terminal-size-devel
%endif
# for missing dep 'hls-alternate-number-format-plugin':
BuildRequires:  ghc-syb-devel
# for missing dep 'hls-cabal-plugin':
%if 0%{?fedora} >= 39
BuildRequires:  ghc-Cabal-syntax-devel
%endif
# for missing dep 'hls-change-type-signature-plugin':
BuildRequires:  ghc-syb-devel
# for missing dep 'hls-code-range-plugin':
%if %{defined fedora}
BuildRequires:  ghc-semigroupoids-devel
%endif
BuildRequires:  ghc-vector-devel
# for missing dep 'hls-eval-plugin':
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-dlist-devel
%if %{defined fedora}
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-parser-combinators-devel
BuildRequires:  ghc-pretty-simple-devel
%endif
BuildRequires:  ghc-time-devel
%if %{defined fedora}
BuildRequires:  ghc-unliftio-devel
%endif
# for missing dep 'hls-explicit-record-fields-plugin':
BuildRequires:  ghc-syb-devel
# for missing dep 'hls-graph':
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-js-dgtable-devel
BuildRequires:  ghc-js-flot-devel
BuildRequires:  ghc-js-jquery-devel
BuildRequires:  ghc-time-devel
%if %{defined fedora}
BuildRequires:  ghc-unliftio-devel
%endif
# for missing dep 'hls-hlint-plugin':
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-ghc-lib-parser-devel
BuildRequires:  ghc-ghc-lib-parser-ex-devel
BuildRequires:  ghc-hlint-devel
BuildRequires:  ghc-refact-devel
# for missing dep 'hls-ormolu-plugin':
BuildRequires:  ghc-ormolu-devel
# for missing dep 'hls-overloaded-record-dot-plugin':
BuildRequires:  ghc-syb-devel
# for missing dep 'hls-plugin-api':
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-dlist-devel
%if %{defined fedora}
BuildRequires:  ghc-lens-aeson-devel
BuildRequires:  ghc-megaparsec-devel
%endif
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unliftio-devel
# for missing dep 'hls-qualify-imported-names-plugin':
BuildRequires:  ghc-dlist-devel
# for missing dep 'hls-refactor-plugin':
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-ghc-boot-devel
BuildRequires:  ghc-parser-combinators-devel
BuildRequires:  ghc-regex-applicative-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-time-devel
# for missing dep 'hls-rename-plugin':
BuildRequires:  ghc-syb-devel
# for missing dep 'hls-splice-plugin':
BuildRequires:  ghc-dlist-devel
%if %{defined fedora}
BuildRequires:  ghc-foldl-devel
%endif
BuildRequires:  ghc-syb-devel
# for missing dep 'hw-prim':
BuildRequires:  ghc-mmap-devel
BuildRequires:  ghc-vector-devel
# for missing dep 'implicit-hie':
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-filepattern-devel
BuildRequires:  ghc-yaml-devel
# for missing dep 'integer-conversion':
BuildRequires:  ghc-primitive-devel
# for missing dep 'list-t':
BuildRequires:  ghc-foldl-devel
BuildRequires:  ghc-logict-devel
BuildRequires:  ghc-mmorph-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-transformers-base-devel
# for missing dep 'lsp':
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-lens-aeson-devel
BuildRequires:  ghc-random-devel
%if %{defined fedora}
BuildRequires:  ghc-uuid-devel
%endif
# for missing dep 'lsp-types':
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-indexed-traversable-devel
BuildRequires:  ghc-indexed-traversable-instances-devel
BuildRequires:  ghc-lens-aeson-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-safe-devel
%if 0%{?fedora} >= 38
BuildRequires:  ghc-some-devel
%endif
BuildRequires:  ghc-template-haskell-devel
# for missing dep 'mod':
BuildRequires:  ghc-ghc-bignum-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-vector-devel
# for missing dep 'monad-dijkstra':
BuildRequires:  ghc-free-devel
BuildRequires:  ghc-psqueues-devel
# for missing dep 'opentelemetry':
BuildRequires:  ghc-exceptions-devel
# for missing dep 'primitive-extras':
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-deferred-folds-devel
BuildRequires:  ghc-foldl-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-vector-devel
# for missing dep 'primitive-unlifted':
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-text-short-devel
# for missing dep 'process-extras':
BuildRequires:  ghc-generic-deriving-devel
# for missing dep 'random-shuffle':
%if %{defined fedora}
BuildRequires:  ghc-MonadRandom-devel
%endif
BuildRequires:  ghc-random-devel
# for missing dep 'regex':
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-regex-base-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-locale-compat-devel
BuildRequires:  ghc-utf8-string-devel
# for missing dep 'regex-pcre-builtin':
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-regex-base-devel
# for missing dep 'retrie':
BuildRequires:  ghc-ansi-terminal-devel
%if %{defined fedora}
BuildRequires:  ghc-haskell-src-exts-devel
%endif
BuildRequires:  ghc-syb-devel
# for missing dep 'row-types':
BuildRequires:  ghc-constraints-devel
BuildRequires:  ghc-profunctors-devel
# for missing dep 'semirings':
BuildRequires:  ghc-base-compat-batteries-devel
# for missing dep 'sqlite-simple':
%if %{defined fedora}
BuildRequires:  ghc-Only-devel
%endif
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-blaze-builder-devel
%if %{defined fedora}
BuildRequires:  ghc-blaze-textual-devel
%endif
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-time-devel
# for missing dep 'stm-containers':
BuildRequires:  ghc-deferred-folds-devel
# for missing dep 'stm-hamt':
BuildRequires:  ghc-deferred-folds-devel
BuildRequires:  ghc-primitive-devel
# for missing dep 'stylish-haskell':
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HsYAML-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-ghc-lib-parser-devel
BuildRequires:  ghc-ghc-lib-parser-ex-devel
BuildRequires:  ghc-strict-devel
BuildRequires:  ghc-syb-devel
# for missing dep 'text-rope':
BuildRequires:  ghc-vector-devel
%endif
# End cabal-rpm deps

%if %[v"%{ghc_version}" < v"9.4"]
BuildRequires: gcc-c++
%endif
%if %[v"%{ghc_version}" > v"9.4"]
BuildRequires:  cabal-install > 3.8
%elif %[v"%{ghc_version}" > v"9.2"]
BuildRequires:  cabal-install > 3.6
%elif %[v"%{ghc_version}" > v"9.0"]
BuildRequires:  cabal-install > 3.4
%else
BuildRequires:  cabal-install > 3.2
%endif

%if %{wrapper_pkg}
Requires: haskell-language-server-wrapper = %{version}-%{release}
%else
Requires: haskell-language-server-wrapper = %{version}
%endif
%if %{defined ghc_version}
Requires: %{ghc_prefix} = %{ghc_version}
%endif
Recommends: cabal-install
#Recommends: stack
%if %{defined ghc_name}
%if %[v"%{ghc_version}" > v"9.2"]
Obsoletes: haskell-language-server-%{ghc_name}-9.2.4 < %{version}-%{release}
%elif %[v"%{ghc_version}" > v"9.0"]
Obsoletes: haskell-language-server-%{ghc_name}-9.0.2 < %{version}-%{release}
%else
Obsoletes: haskell-language-server-%{ghc_name}-8.10.7 < %{version}-%{release}
Obsoletes: haskell-language-server-8.10.7 < %{version}-%{release}
%endif
%else
Obsoletes: haskell-language-server-%{?ghc_version} < %{version}-%{release}
%endif

%description
The Haskell language server (LSP) built for GHC %{ghc_version}.

Please see the README on GitHub at
<https://github.com/haskell/haskell-language-server#readme>.


%if %{wrapper_pkg}
%package -n haskell-language-server-wrapper
Summary: Haskell LSP server wrapper


%description -n haskell-language-server-wrapper
The Haskell language server (LSP) wrapper

Please see the README on GitHub at
<https://github.com/haskell/haskell-language-server#readme>.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
%if %{undefined ghc_name}
%if 0%{?fedora} < 38
%patch -P1 -p1 -b .orig
%endif
%endif
# End cabal-rpm setup
cabal-tweak-flag dynamic False

%if %[v"%{ghc_version}" < v"9.4"]
cabal-tweak-flag hlint False
%endif

cabal update %{!?_with_compiler_default:-w ghc-%{ghc_version}}


%build
# Begin cabal-rpm build:
# End cabal-rpm build


%install
%ghc_set_gcc_flags
# Begin cabal-rpm install
mkdir -p %{buildroot}%{_bindir}
cabal install %{!?_with_compiler_default:-w ghc-%{ghc_version}} --install-method=copy --enable-executable-stripping --installdir=%{buildroot}%{_bindir}
mv %{buildroot}%{_bindir}/{%{pkg_name},%{executable}}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
%{buildroot}%{_bindir}/%{executable} --bash-completion-script %{executable} | sed s/filenames/default/ > %{buildroot}%{_datadir}/bash-completion/completions/%{executable}
%if %{wrapper_pkg}
%{buildroot}%{_bindir}/haskell-language-server-wrapper --bash-completion-script haskell-language-server-wrapper | sed s/filenames/default/ > %{buildroot}%{_datadir}/bash-completion/completions/haskell-language-server-wrapper
%else
rm %{buildroot}%{_bindir}/haskell-language-server-wrapper
%endif
# End cabal-rpm install


%files
# Begin cabal-rpm files:
%license LICENSE
%doc ChangeLog.md README.md
%{_bindir}/%{executable}
%{_datadir}/bash-completion/completions/%{executable}
# End cabal-rpm files


%if %{wrapper_pkg}
%files -n haskell-language-server-wrapper
%{_bindir}/haskell-language-server-wrapper
%{_datadir}/bash-completion/completions/haskell-language-server-wrapper
%endif


%changelog
* Fri Nov 24 2023 Jens Petersen <petersen@redhat.com> - 2.4.0.0-3.ghc%{ghc_minor}
- build wrapper with ghc9.2 for before Fedora 38 (ie ghc-8.10.7 releases)

* Thu Nov 23 2023 Jens Petersen <petersen@redhat.com> - 2.4.0.0-2.ghc%{ghc_minor}
- add ghc minor version suffix to release

* Sun Oct 22 2023 Jens Petersen <petersen@redhat.com> - 2.4.0.0-1
- https://hackage.haskell.org/package/haskell-language-server-2.4.0.0/changelog

* Fri Sep 29 2023 Jens Petersen <petersen@redhat.com> - 2.3.0.0-1
- https://hackage.haskell.org/package/haskell-language-server-2.3.0.0/changelog
- Provides haskell-language-server-ghc-X.Y.Z

* Sat Aug 12 2023 Jens Petersen <petersen@redhat.com> - 2.1.0.0-1
- https://hackage.haskell.org/package/haskell-language-server-2.1.0.0/changelog

* Tue Aug  8 2023 Jens Petersen <petersen@redhat.com> - 2.0.0.1-1
- https://hackage.haskell.org/package/haskell-language-server-2.0.0.1/changelog

* Tue Jun 13 2023 Jens Petersen <petersen@redhat.com> - 2.0.0.0-2
- upstream patch for eval plugin Monad constraint

* Sat May 20 2023 Jens Petersen <petersen@redhat.com> - 2.0.0.0-1
- https://hackage.haskell.org/package/haskell-language-server-2.0.0.0/changelog

* Sun Apr  2 2023 Jens Petersen <petersen@redhat.com> - 1.10.0.0-1
- https://hackage.haskell.org/package/haskell-language-server-1.10.0.0/changelog

* Sat Feb 25 2023 Jens Petersen <petersen@redhat.com> - 1.9.1.0-1
- https://hackage.haskell.org/package/haskell-language-server-1.9.1.0/changelog

* Tue Dec 27 2022 Jens Petersen <petersen@redhat.com> - 1.9.0.0-1
- https://github.com/haskell/haskell-language-server/releases/tag/1.9.0.0
- https://hackage.haskell.org/package/haskell-language-server-1.9.0.0/changelog
- disable call-hierarchy plugin until Hackage updated

* Tue Nov 29 2022 Jens Petersen <petersen@redhat.com> - 1.8.0.0-4
- fixup obsoletes correctly using ghc_version

* Mon Nov 28 2022 Jens Petersen <petersen@redhat.com> - 1.8.0.0-3
- fix obsoletes for haskell-language-server-8.10.*

* Sat Nov 26 2022 Jens Petersen <petersen@redhat.com> - 1.8.0.0-2
- revert to unversioned binary package name

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
