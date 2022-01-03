%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname procs
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A modern replacement for ps written in Rust
License:        MIT
URL:            https://github.com/dalance/procs
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ cargo

%description
procs is a replacement for ps written in Rust.

%prep
%autosetup -n %{appname}-master -p1

%build
cargo build --release

%install
install -pDm0755 target/release/procs %{buildroot}%{_bindir}/procs

%if %{with check}
%check
cargo test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%changelog
