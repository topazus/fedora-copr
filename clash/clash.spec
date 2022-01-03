%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname clash

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A rule-based tunnel in Go
License:        GPL
URL:            https://github.com/Dreamacro/clash
Source:         https://github.com/Dreamacro/clash/archive/master/%{appname}-master.tar.gz

BuildRequires: golang git gcc
BuildRequires: wget

%description
A rule-based tunnel in Go.

%prep
%autosetup -n %{appname}-master -p1

mkdir -p $HOME/go-env
wget -O- https://golang.org/dl/go1.16.5.linux-amd64.tar.gz | tar xvzf - -C $HOME/go-env

%build
$HOME/go-env/go/bin/go build

%install
install -pDm755 clash %{buildroot}%{_bindir}/clash

%check
$HOME/go-env/go/bin/go test github.com/Dreamacro/clash/...

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%changelog
