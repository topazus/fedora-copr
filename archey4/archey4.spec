
%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname archey4
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Archey is a simple system information tool written in Python

License:        GPLv3
URL:            https://github.com/HorlogeSkynet/archey4
Source0:        %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires:  python3-devel python3-pytest
BuildRequires:  (python3dist(distro) >= 1.3 with python3dist(distro) < 2)
BuildRequires:  (python3dist(netifaces) >= 0.10 with python3dist(netifaces) < 1)
BuildRequires:  python3dist(setuptools)

Requires:       (python3dist(distro) >= 1.3 with python3dist(distro) < 2)
Requires:       (python3dist(netifaces) >= 0.10 with python3dist(netifaces) < 1)
Requires:       python3dist(setuptools)

%description
A simple system information tool written in Python.

%prep
%autosetup -n %{appname}-master -p1

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
%pytest
%endif

%files
%license LICENSE
%{_bindir}/archey
%{python3_sitelib}/archey
%{python3_sitelib}/*.egg-info

%dir %{_datadir}/doc/archey4
%{_datadir}/doc/archey4/*.md

%changelog
