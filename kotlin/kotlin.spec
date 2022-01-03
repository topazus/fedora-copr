
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname kotlin

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A modern programming language that makes developers happier
License:        APACHE-2.0
URL:            https://github.com/JetBrains/kotlin
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires:  java-11-openjdk-devel ncurses-compat-libs

Requires:  java-11-openjdk


%description
A modern programming language that makes developers happier.

%prep
%autosetup -n %{appname}-master -p1

%build
JAVA_HOME=%{_jvmdir}/java-1.8.0 \
JDK_16=%{_jvmdir}/java-1.8.0 \
JDK_17=%{_jvmdir}/java-1.8.0 \
JDK_18=%{_jvmdir}/java-1.8.0 \
JDK_9=%{_jvmdir}/java-11 \
JDK_10=%{_jvmdir}/java-11 \
JDK_11=%{_jvmdir}/java-11 \
./gradlew :kotlin-native:dist

%install


%check


appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{python3_sitearch}
%{python3_sitelib}
%{_datadir}
%{_metainfodir}/*.xml

%changelog
