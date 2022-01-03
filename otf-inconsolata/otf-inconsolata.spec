%global debug_package %{nil}

Name:           otf-inconsolata
Version:        3.000
Release:        1%{?dist}
Summary:        Inconsolata fonts
License:        OFL
URL:            https://github.com/googlefonts/Inconsolata
Source:         https://github.com/googlefonts/Inconsolata/releases/download/v%{version}/fonts_otf.zip

BuildRequires: gcc-c++ make pkg-config

%description
A monospace font, designed for code listings and the like, in print.

%prep
%autosetup -n fonts -p1

%build

%install
install -d %{buildroot}%{_datadir}/fonts/%{name}
install -pDm644 otf/Inconsolata-Bold.otf -t %{buildroot}%{_datadir}/fonts/%{name}
install -pDm644 otf/Inconsolata-Light.otf -t %{buildroot}%{_datadir}/fonts/%{name}
install -pDm644 otf/Inconsolata-Medium.otf -t %{buildroot}%{_datadir}/fonts/%{name}
install -pDm644 otf/Inconsolata-Regular.otf -t %{buildroot}%{_datadir}/fonts/%{name}
install -pDm644 otf/Ligconsolata-Bold.otf -t %{buildroot}%{_datadir}/fonts/%{name}
install -pDm644 otf/Ligconsolata-Regular.otf -t %{buildroot}%{_datadir}/fonts/%{name}

%check


%files
%dir %{_datadir}/fonts/%{name}
%{_datadir}/fonts/%{name}/*.otf

%changelog
