%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global _name zola

Name:          %{_name}-git
Version:       0.0.0
Release:       %{build_timestamp}%{?dist}
Summary:       Fast static site generator in a single binary with everything built-in
License:       MIT and ASL 2.0
URL:           https://github.com/getzola/zola
Source0:       %{url}/archive/master/%{_name}-master.tar.gz

BuildRequires: cargo gcc-g++

%description
A fast static site generator in a single binary with everything built-in.

%prep
%autosetup -n %{_name}-master -p1


%build
cargo build --release

%install
install -p -D -m755 target/release/zola   %{buildroot}%{_bindir}/zola

install -Dp -m0644 completions/zola.bash %{buildroot}%{_datadir}/bash-completion/completions/%{_name}
install -Dp -m0644 completions/_zola %{buildroot}%{_datadir}/zsh/site-functions/_%{_name}
install -Dp -m0644 completions/zola.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{_name}.fish

%check
cargo test --release

%files
%license LICENSE
%doc README.md
%{_bindir}/zola
%{_datadir}/bash-completion/completions/%{_name}
%{_datadir}/zsh/site-functions/_%{_name}
%{_datadir}/fish/vendor_completions.d/%{_name}.fish

%changelog
