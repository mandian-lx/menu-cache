Summary:	A library to speed up freedesktop.org application menus
Name:		menu-cache
Version:	0.3.2
Release:	5
License:	GPLv2+
Group:		Graphical desktop/Other
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.gz
Patch0:		menu-cache-0.2.3-fix-str-fmt.patch
URL:		http://lxde.sourceforge.net/
BuildRequires:	glib2-devel
BuildRequires:	intltool

%description
Libmenu-cache is a library creating and utilizing caches to speed up
freedesktop.org application menus.
It can be used as a replacement of libgnome-menu of gnome-menus.

Advantages:
1. Faster loading of menus.
2. Ease of use. (API is very similar to that of libgnome-menu)
3. Lightweight runtime library. (Parsing of the menu definition files
   are done by menu-cache-gen when the menus are really changed.)
4. Less unnecessary and complicated file monitoring.
5. Greatly reduced disk I/O.

%files
%{_libexecdir}/menu-cache*

#----------------------------------------------------------------------

%define major 1
%define libname %mklibname %{name} %{major}

%package -n %{libname}
Group:		Graphical desktop/Other
Requires:	%{name} >= %{version}
Summary:	Contains shared libraries for %{name}

%description -n %{libname}
This package contains shared libraries for %{name}.

%files -n %{libname}
%{_libdir}/*.so.%{major}*

#----------------------------------------------------------------------

%define develname %mklibname -d %{name}

%package -n %{develname}
Group:		Graphical desktop/Other
Requires:	%{libname} = %{version}
Summary:	Contains development files for %{name}
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}

%description -n %{develname}
This package contains development files for %{name}.

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------
%prep
%setup -q
%patch0 -p0

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}


%changelog
* Wed May 30 2012 Andrey Bondrov <abondrov@mandriva.org> 0.3.2-4
+ Revision: 801210
- Don't use find_lang here, it does nothing
- Rebuild to get rid of .la file, spec cleanup

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-3
+ Revision: 666416
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-2mdv2011.0
+ Revision: 606637
- rebuild

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - change lib package requires to ease future major changes (tip from Anssi)

* Sun Feb 28 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.3.2-1mdv2010.1
+ Revision: 512516
- new upstream release 0.3.2

* Tue Feb 16 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.3.1-1mdv2010.1
+ Revision: 506650
- new upstream release 0.3.1

* Sun Feb 14 2010 Funda Wang <fwang@mandriva.org> 0.3.0-1mdv2010.1
+ Revision: 505931
- new version 0.3.0

* Mon Nov 09 2009 Frederik Himpe <fhimpe@mandriva.org> 0.2.6-1mdv2010.1
+ Revision: 463694
- update to new version 0.2.6

* Fri Jul 31 2009 Frederic Crozat <fcrozat@mandriva.com> 0.2.5-2mdv2010.0
+ Revision: 405083
- Ensure libraries are not duplicated in main package

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 0.2.5-1mdv2010.0
+ Revision: 369562
- fix file list
- New version 0.2.5

* Tue Apr 21 2009 Funda Wang <fwang@mandriva.org> 0.2.4-1mdv2009.1
+ Revision: 368476
- New version 0.2.4

* Mon Apr 06 2009 Funda Wang <fwang@mandriva.org> 0.2.3-1mdv2009.1
+ Revision: 364363
- New version 0.2.3

* Thu Dec 11 2008 Funda Wang <fwang@mandriva.org> 0.2.2-1mdv2009.1
+ Revision: 312650
- New version 0.2.2

* Wed Dec 10 2008 Funda Wang <fwang@mandriva.org> 0.2.1-1mdv2009.1
+ Revision: 312478
- New versino 0.2.1

* Fri Nov 28 2008 Funda Wang <fwang@mandriva.org> 0.1.2-1mdv2009.1
+ Revision: 307390
- new version 0.1.2

* Fri Nov 28 2008 Funda Wang <fwang@mandriva.org> 0.1.1-1mdv2009.1
+ Revision: 307342
- import menu-cache


