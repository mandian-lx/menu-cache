Summary:	A library to speed up freedesktop.org application menus
Name:     	menu-cache
Version:	0.2.6
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
Patch0:		menu-cache-0.2.3-fix-str-fmt.patch
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
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

%files -f %{name}.lang
%defattr(-, root, root)
%{_libexecdir}/menu-cache*

#----------------------------------------------------------------------

%define major 0
%define libname %mklibname %name %major
%package -n %libname
Group:		Graphical desktop/Other
Requires:	%name = %version
Summary:	Contains shared libraries for %name

%description -n %libname
This package contains shared libraries for %name.

%files -n %libname
%defattr(-, root, root)
%{_libdir}/*.so.%{major}*

#----------------------------------------------------------------------

%define develname %mklibname -d %name
%package -n %develname
Group:		Graphical desktop/Other
Requires:	%libname = %version
Summary:	Contains development files for %name
Provides:       %name-devel = %version
Provides:       lib%name-devel = %version

%description -n %develname
This package contains development files for %name.

%files -n %develname
%defattr(-, root, root)
%_libdir/*.la
%_libdir/*.so
%_includedir/%name
%_libdir/pkgconfig/*.pc

#----------------------------------------------------------------------
%prep
%setup -q -n %name-%version
%patch0 -p0

%build
%configure2_5x --disable-static
%make

%install
rm -rf %buildroot
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf %buildroot
