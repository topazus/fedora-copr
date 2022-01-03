%global debug_package %{nil}
%global appname go

Name:           golang-bin
Version:        1.17.1
Release:        1%{?dist}
Summary:        The Go Programming Language
License:        BSD
URL:            https://go.dev/
Source:         https://go.dev/dl/go%{version}.linux-amd64.tar.gz

BuildRequires:  pkg-config

%description
Go is an open source programming language that makes it easy to build simple, reliable, and efficient software.

%prep
%autosetup -n %{appname} -p1

%build


%install
mkdir -p %{buildroot}/opt/go
cp -a * %{buildroot}/opt/go

%check


%files
%license LICENSE*
%doc README.md
%dir /opt/go
/opt/go/*

%changelog
