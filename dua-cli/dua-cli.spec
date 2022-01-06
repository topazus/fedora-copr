%global debug_package %{nil}
%global build_date %{lua: print(os.date("%Y.%m.%d"))}
%global appname dua-cli

Name:           %{appname}-git
Version:        %{build_date}
Release:        1%{?dist}
Summary:        View disk space usage and delete unwanted data fast
License:        MIT
URL:            https://github.com/Byron/dua-cli
Source:         %{url}/archive/main/%{appname}-main.tar.gz

BuildRequires:  gcc-c++ make pkg-config
%if 0%{?fedora} >= 34 && 0%{?centos} >= 9
BuildRequires:  rust cargo
%endif

%description
dua (-> Disk Usage Analyzer) is a tool to conveniently learn about the usage of disk space of a given directory. It's parallel by default and will max out your SSD, providing relevant information as fast as possible. Optionally delete superfluous data, and do so more quickly than rm.

%prep
%autosetup -n %{appname}-main -p1

%if 0%{?centos} < 9
if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi
%endif

%build
%if 0%{?fedora} >= 34 && 0%{?centos} >= 9
cargo build --release
%elif 0%{?centos} < 9
$HOME/.cargo/bin/cargo build --release
%endif

%install
install -pDm755 target/release/dua %{buildroot}%{_bindir}/dua

%check
cargo test

%files
%license LICENSE*
%doc README.md
%{_bindir}/dua

%changelog
