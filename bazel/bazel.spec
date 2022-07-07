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

BuildRequires:  zlib-devel
BuildRequires:  pkgconfig
BuildRequires:  gcc-c++
BuildRequires:  which
BuildRequires:  unzip zip

BuildRequires:  python3 python-absl-py

Requires:       java-11-openjdk-devel

%description
Correct, reproducible, and fast builds for everyone.

%prep
%setup -q -c -n bazel-%{version}

%build
bash compile.sh
bash scripts/generate_bash_completion.sh --bazel=output/bazel --output=output/bazel.bash
python scripts/generate_fish_completion.py --bazel=output/bazel --output=output/bazel.fish

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions

install -pDm755 output/bazel %{buildroot}%{_bindir}/bazel-real
install -pDm755 scripts/packages/bazel.sh %{buildroot}%{_bindir}/bazel

install -pDm644 output/bazel-complete.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -pDm644 scripts/zsh_completion/_bazel %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -pDm644 output/bazel.fish %{buildroot}%{_datadir}/fish/vendor_conf.d/%{name}.fish

%files
%{_bindir}/bazel
%{_bindir}/bazel-real

%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/fish/vendor_conf.d/%{name}.fish

%changelog
