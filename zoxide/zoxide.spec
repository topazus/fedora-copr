%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname zoxide

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Faster way to navigate your filesystem
License:        MIT
URL:            https://github.com/ajeetdsouza/zoxide
Source:         %{url}/archive/main/%{appname}-main.tar.gz

%if 0%{?fedora} >= 34
BuildRequires:  rust cargo
%endif

%description
Faster way to navigate your filesystem.

%prep
%autosetup -n %{appname}-main -p1

%if 0%{?centos} <= 8
if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi
%endif

%build
%if 0%{?fedora} >= 34
cargo build --release
%elif 0%{?centos} <= 8
$HOME/.cargo/bin/cargo build --release
%endif

%install
install -pDm755 target/release/%{appname} %{buildroot}%{_bindir}/%{appname}

install -pDm644 contrib/completions/zoxide.bash %{buildroot}%{_datadir}/bash-completion/completions/zoxide
install -pDm644 zoxide.plugin.zsh %{buildroot}%{_datadir}/zsh/site-functions/_zoxide
install -pDm644 init.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/zoxide.fish

%check
cargo test

%files
%license LICENSE
%doc README.md
%{_bindir}/zoxide
%{_datadir}/bash-completion/completions/zoxide
%{_datadir}/fish/vendor_completions.d/zoxide.fish
%{_datadir}/zsh/site-functions/_zoxide

%changelog
