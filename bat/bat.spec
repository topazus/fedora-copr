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
Source:         https://github.com/sharkdp/bat/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ pkg-config rust-packaging

%description
A cat(1) clone with syntax highlighting and Git integration.

%prep
%autosetup -n %{appname}-master -p1

%build
cargo build --release

%install
install -pDm755 target/release/%{appname} %{buildroot}%{_bindir}/%{appname}

gzip -9k assets/manual/bat.1.in
install -pDm644 assets/manual/bat.1.in.gz %{buildroot}%{_mandir}/%{appname}.1.gz

install -pDm644 assets/completions/bat.bash.in \
    %{buildroot}%{_datadir}/bash-completion/completions/%{appname}

install -pDm644 assets/completions/bat.zsh.in \
    %{buildroot}%{_datadir}/zsh/site-functions/_%{appname}

install -pDm644 assets/completions/bat.fish.in \
    %{buildroot}%{_datadir}/fish/vendor_completions.d/%{appname}.fish

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
