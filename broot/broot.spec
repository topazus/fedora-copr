%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname broot
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A better way to see and navigate directory trees
License:        MIT
URL:            https://github.com/Canop/broot
Source:         https://github.com/Canop/broot/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ make pkg-config cargo

%description
A better way to see and navigate directory trees.

%prep
%autosetup -n %{appname}-master -p1

%build
cargo build --release

%install
install -pDm755 target/release/broot %{buildroot}%{_bindir}/broot

gzip --best man/page
install -pDm644 man/page.gz %{buildroot}%{_datadir}/man/man1/broot.1.gz

%if %{with check}
%check
cargo test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/man/man1/broot.1.gz

%changelog
