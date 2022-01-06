%bcond_without check
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global debug_package %{nil}
%global appname bat

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Cat(1) clone with wings

License:        ASL 2.0 or MIT
URL:            https://github.com/sharkdp/bat
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ pkg-config
%if 0%{?fedora} >= 34 && 0%{?centos} >= 9
BuildRequires:  rust cargo
%endif

%description
A cat(1) clone with syntax highlighting and Git integration.

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
install -pDm755 target/release/%{appname} %{buildroot}%{_bindir}/%{appname}

install -pDm644 assets/manual/bat.1.in %{buildroot}%{_mandir}/%{appname}.1

install -pDm644 assets/completions/bat.bash.in %{buildroot}%{_datadir}/bash-completion/completions/%{appname}

install -pDm644 assets/completions/bat.zsh.in %{buildroot}%{_datadir}/zsh/site-functions/_%{appname}

install -pDm644 assets/completions/bat.fish.in %{buildroot}%{_datadir}/fish/vendor_completions.d/%{appname}.fish

%if %{with check}
%check
cargo test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%{_mandir}/%{appname}.1.gz
%{_datadir}/bash-completion/completions/%{appname}
%{_datadir}/zsh/site-functions/_%{appname}
%{_datadir}/fish/vendor_completions.d/%{appname}.fish

%changelog
