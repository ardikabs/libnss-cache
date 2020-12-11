Name:           libnss-cache
Version:        0.17
Release:        1%{?dist}
Summary:        a NSS module for reading directory service information for Linux hosts from an indexed, local disk cache of that directory service

License:        GPLv3+
URL:            https://github.com/google/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

%description
NSS module for using nsscache-generated files
 This package provides a Name Service Switch module that uses .cache
 files as a name service. This means providing user account
 information, group ids, netgroups, and automounts.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT LIBDIR=$RPM_BUILD_ROOT/usr/lib64

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/*.so*

%changelog
* Tue Jan 14 2020 Jamie Wilkinson <jaq@debian.org> - 0.17-1
- New upstram release.
- Trim trailing whitespace.
- Bump debhelper from old 9 to 12.
- Set debhelper-compat version in Build-Depends.
- Use canonical URL in Vcs-Git.
