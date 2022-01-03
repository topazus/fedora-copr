%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname cpufetch

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Simple yet fancy CPU architecture fetching tool
License:        MIT
URL:            https://github.com/Dr-Noob/cpufetch
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc make pkg-config

%description
cpufetch is a command-line tool written in C that displays the CPU information in a clean and beautiful way

%prep
%autosetup -n %{appname}-master -p1

%build
make

%install
install -pDm755 cpufetch %{buildroot}%{_bindir}/cpufetch
gzip --best cpufetch.1
install -pDm644 cpufetch.1.gz %{buildroot}%{_datadir}/man/man1/cpufetch.1.gz

%check


%files
%license LICENSE
%doc README.md
%{_bindir}/cpufetch
%{_datadir}/man/man1/cpufetch.1.gz

%changelog
