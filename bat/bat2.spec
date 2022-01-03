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

BuildRequires:  gcc-c++ cargo

%description
A cat(1) clone with syntax highlighting and Git integration.

%prep
%autosetup -n %{appname}-master -p1

%build
cargo build --release

%install
install -pDm755 target/release/%{appname} %{buildroot}%{_bindir}/%{appname}

find . -name bat.1 -type f -exec install -pDm644 {} \
%{buildroot}%{_mandir}/bat.1 \;

find . -name bat.bash -type f -exec install -pDm644 {} \
%{buildroot}%{_datadir}/bash-completion/completions/bat \;

find . -name bat.zsh -type f -exec install -pDm644 {} \
%{buildroot}%{_datadir}/zsh/site-functions/_bat \;

find . -name bat.fish -type f -exec install -pDm644 {} \
%{buildroot}%{_datadir}/fish/vendor_completions.d/bat.fish \;

%if %{with check}
%check
cargo test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/bat

%{_mandir}/bat.1
%{_datadir}/bash-completion/completions/bat
%{_datadir}/zsh/site-functions/_bat
%{_datadir}/fish/vendor_completions.d/bat.fish

%changelog
