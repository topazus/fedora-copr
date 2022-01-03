
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname erlang
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        a programming language and runtime system for building massively scalable soft real-time systems
License:        APACHE
URL:            https://github.com/erlang/otp
Source:         https://github.com/erlang/otp/archive/master/otp-master.tar.gz

BuildRequires: gcc-c++ cmake pkg-config perl ncurses-devel

BuildRequires: openssl-devel flex systemd-devel
BuildRequires: lksctp-tools-devel m4 ncurses-devel zlib-devel

Requires: lksctp-tools

%description
Erlang is a programming language and runtime system for building massively scalable soft real-time systems with requirements on high availability.

OTP is a set of Erlang libraries, which consists of the Erlang runtime system, a number of ready-to-use components mainly written in Erlang, and a set of design principles for Erlang programs.

%prep
%autosetup -n otp-master -p1

%build
./otp_build autoconf
./configure --prefix=%{buildroot}%{_prefix} --enable-shared-zlib --enable-sctp --enable-systemd \
    --disable-silent-rules --enable-builtin-zlib --enable-smp-support --with-odbc
make

%install
make install

%if %{with check}
%check
make test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}


%changelog
