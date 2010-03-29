%define name liboobs
%define version 2.30.0
%define release %mkrel 1
%define major 4
%define libname %mklibname oobs-1_ %major
%define libnamedev %mklibname -d oobs-1

Summary: System configuration backend library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/liboobs/%{name}-%{version}.tar.bz2
Patch: liboobs-2.22.2-format-strings.patch
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: dbus-glib-devel
BuildRequires: libhal-devel
BuildRequires: system-tools-backends2 >= 2.9.2
BuildRequires: gtk-doc

%description
Liboobs is a wrapping library to the System Tools Backends, it will
provide easy to access GObjects to system configuration details, like
users, groups and network interfaces, it will handle sessions with the
backend and data consistency too.

%package -n %libname
Group: System/Libraries
Summary: System configuration backend shared library

%description -n %libname
Liboobs is a wrapping library to the System Tools Backends, it will
provide easy to access GObjects to system configuration details, like
users, groups and network interfaces, it will handle sessions with the
backend and data consistency too.

%package -n %libnamedev
Group: Development/C
Summary: Header files of the system configuration backend library
Requires: %libname = %version
Provides: %name-devel = %version-%release
Obsoletes: %mklibname -d oobs-1_ 3

%description -n %libnamedev
Liboobs is a wrapping library to the System Tools Backends, it will
provide easy to access GObjects to system configuration details, like
users, groups and network interfaces, it will handle sessions with the
backend and data consistency too.


%prep
%setup -q
%patch -p1

%build
%configure2_5x  --enable-gtk-doc
#gw parallel build broken in 2.29.3
make


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std


%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS NEWS README ChangeLog
%_libdir/liboobs-1.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%_datadir/gtk-doc/html/liboobs
%_includedir/liboobs-1.0/
%_libdir/liboobs-1.a
%attr(644,root,root) %_libdir/liboobs-1.la
%_libdir/liboobs-1.so
%_libdir/pkgconfig/liboobs-1.pc
