%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname wezterm

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A GPU-accelerated cross-platform terminal emulator and multiplexer
License:        MIT
URL:            https://github.com/wez/wezterm
Source:         https://github.com/wez/wezterm/archive/main/wezterm-main.tar.gz

BuildRequires:  make gcc gcc-c++ cmake
BuildRequires:  fontconfig-devel openssl-devel perl-interpreter python3
BuildRequires:  libxcb-devel libxkbcommon-devel libxkbcommon-x11-devel wayland-devel mesa-libEGL-devel
BuildRequires:  xcb-util-devel xcb-util-keysyms-devel xcb-util-image-devel xcb-util-wm-devel
BuildRequires:  git desktop-file-utils

Requires:       openssl

%description
A GPU-accelerated cross-platform terminal emulator and multiplexer.

%prep
git clone --depth=1 --branch=main --recursive https://github.com/wez/wezterm.git .
git submodule update --init --recursive

curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y


%build
$HOME/.cargo/bin/cargo build --release


%install
install -pDm755 target/release/wezterm %{buildroot}%{_bindir}/%{appname}
install -pDm755 target/release/wezterm-gui %{buildroot}%{_bindir}/wezterm-gui
install -pDm755 target/release/wezterm-mux-server %{buildroot}%{_bindir}/wezterm-mux-server
install -pDm755 target/release/strip-ansi-escapes %{buildroot}%{_bindir}/strip-ansi-escapes

install -pDm644 assets/wezterm.desktop %{buildroot}%{_datadir}/applications/%{appname}.desktop
install -pDm644 assets/icon/wezterm-icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/wezterm.svg
install -pDm644 assets/icon/terminal.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/wezterm.png

install -pDm644 assets/wezterm.appdata.xml %{buildroot}%{_datadir}/metainfo/%{appname}.appdata.xml


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appname}.desktop

%files
%license LICENSE*
%doc README.md
%{_bindir}/wezterm
%{_bindir}/wezterm-gui
%{_bindir}/wezterm-mux-server
%{_bindir}/strip-ansi-escapes

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/128x128/apps/wezterm.png
%{_datadir}/icons/hicolor/scalable/apps/wezterm.svg
%{_datadir}/metainfo/%{appname}.appdata.xml

%changelog
