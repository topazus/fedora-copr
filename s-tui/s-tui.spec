%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname s-tui
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Terminal-based CPU stress and monitoring utility
License:        GPL-2.0
URL:            https://github.com/amanusk/s-tui
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ python3-setuptools python3-devel
BuildRequires:  python3-pytest python3-urwid python3-psutil

Requires: python3-urwid python3-psutil

Recommends: stress stress-ng

%description
Stress-Terminal UI, s-tui, monitors CPU temperature, frequency, power and utilization in a graphical way from the terminal.

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
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{python3_sitelib}/s_tui/*
%{python3_sitelib}/s_tui-*.egg-info/*

%changelog
