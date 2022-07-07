
%global debug_package %{nil}

Name:           bazel
Version:        5.2.0
Release:        1%{?dist}
Summary:        Correct, reproducible, and fast builds for everyone.
License:        Apache License 2.0
URL:            http://bazel.io/
Source0:        https://github.com/bazelbuild/bazel/releases/download/%{version}/bazel-%{version}-dist.zip

Provides:	bazel

BuildRequires:  java-11-openjdk-devel
#BuildRequires:  java-1_8_0-openjdk-headless ## OpenSUSE
#BuildRequires:  java-1.8.0-openjdk-headless ## Mageia
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig
BuildRequires:  gcc-c++
BuildRequires:  which
BuildRequires:  unzip zip

BuildRequires:  python3

Requires:       java-11-openjdk-devel
#Requires:       java-1_8_0-openjdk-headless ## OpenSUSE
#Requires:       java-1.8.0-openjdk-headless ## Mageia


%description
Correct, reproducible, and fast builds for everyone.

%prep
%setup -q -c -n bazel-%{version}

%build
# loose epoch from their release date
export SOURCE_DATE_EPOCH="$(date -d $(head -1 CHANGELOG.md | %{__grep} -Eo '\b[[:digit:]]{4}-[[:digit:]]{2}-[[:digit:]]{2}\b' ) +%s)"
export EMBED_LABEL="%{version}"

bash ./compile.sh
bash ./scripts/generate_bash_completion.sh --bazel=output/bazel --output=output/bazel-complete.bash

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
install -pDm644 output/bazel %{buildroot}%{_bindir}/bazel-real
install -pDm644 ./scripts/packages/bazel.sh %{buildroot}%{_bindir}/bazel
install -pDm644 output/bazel-complete.bash %{buildroot}%{_datadir}/bash-completion/completions/bazel


%files
%{_bindir}/bazel
%{_bindir}/bazel-real
%{_datadir}/bash-completion/completions/bazel

%changelog
