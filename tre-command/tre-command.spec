
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname tre-command
%bcond_without check

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Tree command, improved
License:        MIT
URL:            https://github.com/dduan/tre
Source:         https://github.com/dduan/tre/archive/main/%{appname}-main.tar.gz

BuildRequires: gcc-c++ make pkg-config
BuildRequires: rust cargo


%description
A modern alternative to the tree command.

%prep
%autosetup -n %{appname}-main -p1

%build
cargo build --release

%install
install -pDm755 target/release/tre %{buildroot}%{_bindir}/tre

gzip -9k manual/tre.1
install -pDm644 manual/tre.1.gz %{buildroot}%{_mandir}/man1/tre.1.gz

%if %{with check}
%check
cargo test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/tre
%{_mandir}/man1/tre.1.gz


%changelog
