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

%description
Yet another cross-platform graphical process/system monitor.

%prep
%autosetup -n %{appname}-master -p1

curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y


%build
$HOME/.cargo/bin/cargo build --release


%install
install -pDm755 target/release/btm %{buildroot}%{_bindir}/%{appname}

%check

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%changelog
