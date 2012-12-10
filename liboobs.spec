%define major 5
%define libname %mklibname oobs-1_ %{major}
%define devname %mklibname -d oobs-1

Summary:	System configuration backend library
Name:		liboobs
Version:	2.32.0
Release:	3
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/liboobs/%{name}-%{version}.tar.bz2
Patch0:		liboobs-2.22.2-format-strings.patch

BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(system-tools-backends-2.0)

%description
Liboobs is a wrapping library to the System Tools Backends, it will
provide easy to access GObjects to system configuration details, like
users, groups and network interfaces, it will handle sessions with the
backend and data consistency too.

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



%changelog
* Tue Jun 05 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.32.0-3
+ Revision: 802704
- rebuild
- cleaned up spec

* Wed Sep 28 2011 Götz Waschk <waschk@mandriva.org> 2.32.0-2
+ Revision: 701632
- rebuild

* Mon Sep 27 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581422
- update to new version 2.32.0

* Mon Aug 30 2010 Götz Waschk <waschk@mandriva.org> 2.31.91-1mdv2011.0
+ Revision: 574499
- new version
- new major

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 2.31.1-1mdv2011.0
+ Revision: 563388
- new version

* Mon Mar 29 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528911
- update to new version 2.30.0

* Tue Mar 09 2010 Götz Waschk <waschk@mandriva.org> 2.29.92-1mdv2010.1
+ Revision: 516895
- update to new version 2.29.92

* Mon Feb 15 2010 Götz Waschk <waschk@mandriva.org> 2.29.91-1mdv2010.1
+ Revision: 506341
- update to new version 2.29.91

* Tue Feb 09 2010 Götz Waschk <waschk@mandriva.org> 2.29.90-1mdv2010.1
+ Revision: 502815
- new version
- update system-tools-backends2 dep

* Tue Jan 26 2010 Götz Waschk <waschk@mandriva.org> 2.29.3-1mdv2010.1
+ Revision: 496513
- new version
- disable parallel build

* Tue Jan 12 2010 Götz Waschk <waschk@mandriva.org> 2.29.2.1-1mdv2010.1
+ Revision: 490163
- new version
- drop patch

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 2.29.2-2mdv2010.1
+ Revision: 489935
- add missing header

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 2.29.2-1mdv2010.1
+ Revision: 489884
- new version
- bump system-tools-backends2 dep

* Wed Dec 09 2009 Götz Waschk <waschk@mandriva.org> 2.29.1-1mdv2010.1
+ Revision: 475422
- update to new version 2.29.1

* Thu Sep 10 2009 Götz Waschk <waschk@mandriva.org> 2.22.2-1mdv2010.0
+ Revision: 437204
- new version
- update patch
- enable docs

* Sun Aug 16 2009 Götz Waschk <waschk@mandriva.org> 2.22.1-1mdv2010.0
+ Revision: 417089
- update to new version 2.22.1

* Mon Jul 27 2009 Götz Waschk <waschk@mandriva.org> 2.22.0-4mdv2010.0
+ Revision: 400504
- fix format strings
- update license

* Sun Jul 27 2008 Thierry Vignaud <tv@mandriva.org> 2.22.0-3mdv2009.0
+ Revision: 250313
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Mar 09 2008 Götz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183040
- new version

* Tue Feb 26 2008 Götz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 175274
- new version

* Tue Feb 12 2008 Götz Waschk <waschk@mandriva.org> 2.21.91-1mdv2008.1
+ Revision: 165741
- new version

* Mon Jan 28 2008 Götz Waschk <waschk@mandriva.org> 2.21.90-1mdv2008.1
+ Revision: 159422
- new version

* Tue Jan 15 2008 Götz Waschk <waschk@mandriva.org> 2.21.5-1mdv2008.1
+ Revision: 152134
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Dec 18 2007 Götz Waschk <waschk@mandriva.org> 2.21.3-1mdv2008.1
+ Revision: 132242
- new version
- bump deps

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 14 2007 Götz Waschk <waschk@mandriva.org> 2.21.2.1-1mdv2008.1
+ Revision: 108782
- new version
- bump deps

* Tue Oct 30 2007 Götz Waschk <waschk@mandriva.org> 2.21.1-1mdv2008.1
+ Revision: 103742
- fix buildrequires
- new version
- new major

* Sat Sep 15 2007 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 85974
- new version

* Tue Sep 04 2007 Götz Waschk <waschk@mandriva.org> 2.19.92-1mdv2008.0
+ Revision: 79027
- new version

* Tue Aug 28 2007 Götz Waschk <waschk@mandriva.org> 2.19.91-1mdv2008.0
+ Revision: 72386
- new version
- new devel name

* Tue Jul 10 2007 Götz Waschk <waschk@mandriva.org> 2.19.0-1mdv2008.0
+ Revision: 50940
- new version

* Tue Apr 17 2007 Götz Waschk <waschk@mandriva.org> 2.18.1-1mdv2008.0
+ Revision: 13610
- new version


* Mon Mar 12 2007 Götz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 141704
- new version

* Thu Mar 01 2007 Götz Waschk <waschk@mandriva.org> 2.17.92-1mdv2007.1
+ Revision: 130305
- new version

* Tue Feb 13 2007 Götz Waschk <waschk@mandriva.org> 2.17.91-1mdv2007.1
+ Revision: 120320
- new version

* Wed Jan 24 2007 Götz Waschk <waschk@mandriva.org> 2.17.90.1-1mdv2007.1
+ Revision: 112721
- new version

* Tue Jan 23 2007 Götz Waschk <waschk@mandriva.org> 2.17.90-1mdv2007.1
+ Revision: 112292
- new version

* Wed Jan 10 2007 Götz Waschk <waschk@mandriva.org> 2.17.5.1-1mdv2007.1
+ Revision: 106915
- new version
- disable doc build

* Tue Jan 09 2007 Götz Waschk <waschk@mandriva.org> 2.17.5-1mdv2007.1
+ Revision: 106385
- new version
- new major
- enable gtk doc build
- bump deps

* Fri Dec 01 2006 Götz Waschk <waschk@mandriva.org> 2.17.3-1mdv2007.1
+ Revision: 89551
- new version

* Mon Nov 27 2006 Götz Waschk <waschk@mandriva.org> 2.17.2-1mdv2007.1
+ Revision: 87607
- new version

* Sun Nov 05 2006 Götz Waschk <waschk@mandriva.org> 0.6.1-1mdv2007.1
+ Revision: 76762
- new version

* Fri Oct 13 2006 Götz Waschk <waschk@mandriva.org> 0.6.0-2mdv2007.1
+ Revision: 63694
- rebuild
- Import liboobs

* Sat Oct 07 2006 Götz Waschk <waschk@mandriva.org> 0.6.0-1mdv2007.1
- bump deps
- New version 0.6.0

* Sun Oct 01 2006 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdv2007.0
- new major
- New version 0.5.0

* Tue Sep 12 2006 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdv2007.0
- new major
- bump deps
- drop patch
- New version 0.4.0

* Sat Aug 05 2006 Götz Waschk <waschk@mandriva.org> 0.2.0-3mdv2007.0
- fix buildrequires

* Fri Aug 04 2006 Götz Waschk <waschk@mandriva.org> 0.2.0-2mdv2007.0
- patch for new dbus

* Fri Aug 04 2006 Götz Waschk <waschk@mandriva.org> 0.2.0-1mdv2007.0
- initial package

