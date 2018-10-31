%define major 5
%define libname %mklibname oobs-1_ %{major}
%define devname %mklibname -d oobs-1

Summary:	System configuration backend library
Name:		liboobs
Version:	3.0.0
Release:	5
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/liboobs/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.bz2
Patch0:		liboobs-2.22.2-format-strings.patch

BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(system-tools-backends-2.0)

%description
Liboobs is a wrapping library to the System Tools Backends, it will
provide easy to access GObjects to system configuration details, like
users, groups and network interfaces, it will handle sessions with the
backend and data consistency too.

It is used by LXQt.

%package -n %{libname}
Group:		System/Libraries
Summary:	System configuration backend shared library

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Group:		Development/C
Summary:	Header files of the system configuration backend library
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q
%apply_patches

%build
autoreconf -fi
%configure \
	--disable-static \
	--enable-gtk-doc

%make LIBS='-lgobject-2.0 -lglib-2.0'

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/liboobs-1.so.%{major}*

%files -n %{devname}
%doc AUTHORS NEWS README ChangeLog
%{_datadir}/gtk-doc/html/liboobs
%{_includedir}/liboobs-1.0/
%{_libdir}/liboobs-1.so
%{_libdir}/pkgconfig/liboobs-1.pc
