%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname crystal

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        The Crystal Programming Language
License:        APACHE
URL:            https://github.com/crystal-lang/crystal
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ gmp-devel libbsd-devel libedit-devel libevent-devel
BuildRequires: libxml2-devel libyaml-devel libstdc++-static
BuildRequires:  make openssl-devel pcre-devel wget tar

Requires:  gcc pcre-devel libevent-devel openssl-devel llvm
Requires:  libxml2-devel libyaml-devel libstdc++-static

%if 0%{?fedora} <= 33
%global llvm_version 0
%else
%global llvm_version 1
%endif

%if !%{llvm_version}
BuildRequires:  llvm10-devel llvm10-static
Requires:       llvm10-devel llvm10-static
%else
BuildRequires:  llvm11-devel llvm11-static
Requires:       llvm11-devel llvm11-static
%endif

%description
Crystal is a general-purpose, object-oriented programming language.
With syntax inspired by Ruby, it is a compiled language with static
type-checking,serving both, humans and computers.

%prep
%autosetup -n %{appname}-master -p1
wget https://github.com/crystal-lang/crystal/releases/download/1.0.0/crystal-1.0.0-1-linux-x86_64.tar.gz
tar xf crystal-*-linux-x86_64.tar.gz

%build
export CRYSTAL="./crystal-1.0.0-1/bin/crystal"
%if !%{llvm_version}
export LLVM_CONFIG="/usr/bin/llvm-config-10-64"
%else
export LLVM_CONFIG="/usr/bin/llvm-config-11-64"
%endif

make

%install
install -pDm644 .build/crystal %{buildroot}%{_bindir}/%{appname}

install -pDm644 man/crystal.1 %{buildroot}%{_datadir}/man/man1/crystal.1.gz
mkdir -p %{buildroot}%{_datadir}/doc/crystal/
cp -r samples/ %{buildroot}%{_datadir}/doc/crystal
install -pDm644 etc/completion.bash %{buildroot}%{_datadir}/bash-completion/completions/*
install -pDm644 etc/completion.zsh %{buildroot}%{_datadir}/zsh/site-functions/*

%check

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/man/man1/crystal.1.gz
%{_datadir}/doc/crystal/*
%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/*

%changelog
