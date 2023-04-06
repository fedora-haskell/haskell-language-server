# generated by cabal-rpm-2.1.0 --standalone
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

#%%global ghc_name ghc9.4
%bcond_without compiler_default

%global ghc_prefix %{?ghc_name}%{!?ghc_name:ghc}

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
Version:        1.10.0.0
Release:        1%{?dist}
Summary:        LSP server for GHC %{ghc_version}

License:        Apache-2.0
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources
Patch0:         haskell-language-server-1.7.0.0-prettyprinter-1.7.patch

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
%if %{defined ghc_name}
BuildRequires:  %{ghc_name}
%if %{with compiler_default}
BuildRequires:  %{ghc_name}-compiler-default
%endif
BuildRequires:  zlib-devel
%else
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
%if %{defined fedora}
BuildRequires:  ghc-fingertree-devel
%endif
#BuildRequires:  ghc-focus-devel
BuildRequires:  ghc-ghc-boot-devel
#BuildRequires:  ghc-ghc-check-devel
#BuildRequires:  ghc-ghc-trace-events-devel
BuildRequires:  ghc-haddock-library-devel
#BuildRequires:  ghc-hie-compat-devel
#BuildRequires:  ghc-implicit-hie-devel
#BuildRequires:  ghc-implicit-hie-cradle-devel
#BuildRequires:  ghc-list-t-devel
#BuildRequires:  ghc-opentelemetry-devel
BuildRequires:  ghc-parallel-devel
%if %{defined fedora}
BuildRequires:  ghc-prettyprinter-ansi-terminal-devel
%endif
BuildRequires:  ghc-random-devel
#BuildRequires:  ghc-sorted-list-devel
#BuildRequires:  ghc-stm-containers-devel
BuildRequires:  ghc-syb-devel
#BuildRequires:  ghc-text-rope-devel
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
BuildRequires:  ghc-hslogger-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-yaml-devel
# for missing dep 'hiedb':
#BuildRequires:  ghc-algebraic-graphs-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-array-devel
#BuildRequires:  ghc-hie-compat-devel
%if %{defined fedora}
BuildRequires:  ghc-lucid-devel
BuildRequires:  ghc-terminal-size-devel
%endif
# for missing dep 'hls-alternate-number-format-plugin':
#BuildRequires:  ghc-hie-compat-devel
BuildRequires:  ghc-syb-devel
# for missing dep 'hls-brittany-plugin':
#BuildRequires:  ghc-brittany-devel
#BuildRequires:  ghc-czipwith-devel
#BuildRequires:  ghc-ghc-exactprint-devel
# for missing dep 'hls-cabal-plugin':
BuildRequires:  ghc-Cabal-devel
# for missing dep 'hls-change-type-signature-plugin':
BuildRequires:  ghc-syb-devel
# for missing dep 'hls-class-plugin':
#BuildRequires:  ghc-ghc-exactprint-devel
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
#BuildRequires:  ghc-stm-containers-devel
BuildRequires:  ghc-time-devel
%if %{defined fedora}
BuildRequires:  ghc-unliftio-devel
%endif
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
#BuildRequires:  ghc-hw-fingertree-devel
%if %{defined fedora}
BuildRequires:  ghc-lens-aeson-devel
BuildRequires:  ghc-megaparsec-devel
%endif
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
%if %{defined fedora}
BuildRequires:  ghc-foldl-devel
%endif
#BuildRequires:  ghc-ghc-exactprint-devel
#BuildRequires:  ghc-retrie-devel
BuildRequires:  ghc-syb-devel
# for missing dep 'lsp':
BuildRequires:  ghc-attoparsec-devel
#BuildRequires:  ghc-co-log-core-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-random-devel
#BuildRequires:  ghc-sorted-list-devel
#BuildRequires:  ghc-text-rope-devel
%if %{defined fedora}
BuildRequires:  ghc-uuid-devel
%endif
# for missing dep 'sqlite-simple':
%if %{defined fedora}
BuildRequires:  ghc-Only-devel
%endif
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-blaze-builder-devel
%if %{defined fedora}
BuildRequires:  ghc-blaze-textual-devel
%endif
#BuildRequires:  ghc-direct-sqlite-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-time-devel
# for missing dep 'lsp-types':
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-exceptions-devel
#BuildRequires:  ghc-mod-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-scientific-devel
%if 0%{?fedora} >= 38
BuildRequires:  ghc-some-devel
%endif
BuildRequires:  ghc-template-haskell-devel
# End cabal-rpm deps
# more missing subdeps
BuildRequires:  ghc-HsYAML-devel
%if %{defined fedora}
BuildRequires:  ghc-MonadRandom-devel
BuildRequires:  ghc-constraints-devel
BuildRequires:  ghc-filemanip-devel
%endif
BuildRequires:  ghc-hashtables-devel
%if %{defined fedora}
BuildRequires:  ghc-haskell-src-exts-devel
%if 0%{?fedora} < 38
BuildRequires:  ghc-indexed-profunctors-devel
%endif
BuildRequires:  ghc-logict-devel
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-microlens-th-devel
%endif
BuildRequires:  ghc-monad-control-devel
%if %{defined fedora}
BuildRequires:  ghc-psqueues-devel
BuildRequires:  ghc-type-equality-devel
%endif
%endif
%if %[v"%{ghc_version}" > v"9.2"]
BuildRequires:  cabal-install > 3.6
%elif %[v"%{ghc_version}" > v"9.0"]
BuildRequires:  cabal-install > 3.4
%else
BuildRequires:  cabal-install > 3.2
%endif

%if %{undefined ghc_name}
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


%if %{undefined ghc_name}
%package wrapper
Summary: Haskell LSP server wrapper
Obsoletes:  haskell-language-server-wrapper-ghc8.10 < %{version}
Obsoletes:  haskell-language-server-wrapper-ghc9.0 < %{version}


%description wrapper
The Haskell language server (LSP) wrapper

Please see the README on GitHub at
<https://github.com/haskell/haskell-language-server#readme>.
%endif

%prep
# Begin cabal-rpm setup:
%autosetup -p1 -n %{pkgver}
# End cabal-rpm setup
cabal-tweak-flag dynamic False
# https://github.com/haskell/haskell-language-server/issues/3427
cabal-tweak-flag callHierarchy False

# for ghc-9.2+ hlint needs to be built with ghc-lib flag
%if %[v"%{ghc_version}" < v"9.0"] || %[v"%{ghc_version}" > v"9.2"]
cabal-tweak-flag hlint False
%endif

# https://github.com/haskell/haskell-language-server/issues/3554
%if %[v"%{ghc_version}" < v"9.2"]
cabal-tweak-flag tactic False
%endif

%if %[v"%{ghc_version}" > v"9.2"]
cabal-tweak-flag stylishHaskell False
%endif

%if %[v"%{ghc_version}" > v"9.4"] && %[v"%{ghc_version}" < v"9.5"]
cabal-tweak-flag floskell False
cabal-tweak-flag rename False
%endif

cabal update

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
%if %{undefined ghc_name}
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


%if %{undefined ghc_name}
%files wrapper
%{_bindir}/haskell-language-server-wrapper
%{_datadir}/bash-completion/completions/haskell-language-server-wrapper
%endif


%changelog
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
