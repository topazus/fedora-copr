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
%if 0%{?fedora} >= 34 && 0%{?centos} >= 9
BuildRequires:  rust cargo
%endif

%description
A new type of shell.

%prep
%autosetup -n %{appname}-main -p1

%if 0%{?centos} < 9
if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi
%endif

%build
%if 0%{?fedora} >= 34 && 0%{?centos} >= 9
cargo build --release --workspace --features=extra
%elif 0%{?centos} < 9
$HOME/.cargo/bin/cargo build --release --workspace --features=extra
%endif


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
