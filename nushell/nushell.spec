%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname nushell

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A new type of shell
License:        MIT
URL:            https://github.com/nushell/nushell
Source:         %{url}/archive/main/%{appname}-main.tar.gz

BuildRequires:  gcc-c++ cmake pkg-config
BuildRequires:  desktop-file-utils
BuildRequires:  libxcb openssl-devel libX11-devel

%description
A new type of shell.

%prep
%autosetup -n %{appname}-main -p1

curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y


%build
$HOME/.cargo/bin/cargo build --release


%install
# binaries
find target/release \
    -maxdepth 1 \
    -executable \
    -type f \
    -exec install -pDm755 -t %{buildroot}%{_bindir} {} +

# remove binaries not present in upstream releases
rm -f %{buildroot}%{_bindir}/table
rm -f %{buildroot}%{_bindir}/nu_plugin_{core,extra}_*

%check

%files
%license LICENSE
%doc README.md
%{_bindir}/nu
%{_bindir}/nu_plugin_*
%{_bindir}/nu_pretty_hex

%changelog
