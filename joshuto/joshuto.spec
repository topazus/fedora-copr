%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname joshuto
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        ranger-like terminal file manager written in Rust
License:        LGPL 3.0
URL:            https://github.com/kamiyaa/joshuto
Source:         %{url}/archive/main/%{appname}-main.tar.gz

BuildRequires: gcc-c++ make pkg-config cargo
BuildRequires: desktop-file-utils libappstream-glib

%description
ranger-like terminal file manager written in Rust.

%prep
%autosetup -n %{appname}-main -p1

%build
cargo build --release

%install
install -pDm755 target/release/joshuto %{buildroot}%{_bindir}/joshuto

%if %{with check}
%check
cargo test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%changelog
