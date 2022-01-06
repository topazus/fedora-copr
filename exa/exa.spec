%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname exa

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A modern replacement for ls
License:        MIT
URL:            https://github.com/ogham/exa
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++

%description
exa is a modern replacement for the venerable file-listing command-line program ls that ships with Unix and Linux operating systems, giving it more features and better defaults.

%prep
%autosetup -n %{appname}-master -p1

curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y


%build
$HOME/.cargo/bin/cargo build --release


%install
install -pDm755 target/release/exa %{buildroot}%{_bindir}/%{appname}

install -pDm644 completions/bash/exa %{buildroot}%{_datadir}/bash-completion/completions/%{appname}
install -pDm644 completions/zsh/_exa %{buildroot}%{_datadir}/zsh/site-functions/_%{appname}
install -pDm644 completions/fish/exa.fish %{buildroot}%{_datadir}/fish/vendor_completion.d/%{appname}.fish

%check


%files
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/bash-completion/completions/%{appname}
%{_datadir}/zsh/site-functions/_%{appname}
%{_datadir}/fish/vendor_completion.d/%{appname}.fish

%changelog
