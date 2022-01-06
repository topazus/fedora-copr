%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname bottom

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Yet another cross-platform graphical process/system monitor
License:        MIT
URL:            https://github.com/ClementTsang/bottom
Source0:        %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ pkg-config
%if 0%{?fedora} >= 34 && 0%{?centos} >= 9
BuildRequires:  rust cargo
%endif

%description
Yet another cross-platform graphical process/system monitor.

%prep
%autosetup -n %{appname}-master -p1

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
install -pDm755 target/release/btm %{buildroot}%{_bindir}/%{appname}

%check
cargo test

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%changelog
