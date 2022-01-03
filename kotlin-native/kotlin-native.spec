
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname kotlin-native

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A modern programming language that makes developers happier
License:        APACHE-2.0
URL:            https://github.com/JetBrains/kotlin
Source:         %{url}/archive/master/kotlin-master.tar.gz

BuildRequires:  java-11-openjdk-devel java-1.8.0-openjdk-devel
BuildRequires:  ncurses-compat-libs

Requires:  java-11-openjdk java-1.8.0-openjdk

%description
A modern programming language that makes developers happier.

%prep
%autosetup -n kotlin-master -p1
echo "kotlin.native.enabled=true" >> local.properties

%build
export PATH=$HOME/jdk-9.0.4+11/bin:$PATH
JAVA_HOME=%{_jvmdir}/java-1.8.0 \
JDK_16=%{_jvmdir}/java-1.8.0 \
JDK_17=%{_jvmdir}/java-1.8.0 \
JDK_18=%{_jvmdir}/java-1.8.0 \
JDK_9=%{_jvmdir}/java-11 \
JDK_10=%{_jvmdir}/java-11 \
JDK_11=%{_jvmdir}/java-11 \
./gradlew :kotlin-native:dist

%install
install -pDm755 kotlin-native/dist/bin/kotlinc-native %{buildroot}/kotlinc-native
install -pDm755 kotlin-native/dist/bin/konanc %{buildroot}/konanc
install -pDm755 kotlin-native/dist/bin/cinterop %{buildroot}/cinterop
install -pDm755 kotlin-native/dist/bin/run_konan %{buildroot}/run_konan

%check

%files
%license LICENSE*
%doc README.md

%changelog
