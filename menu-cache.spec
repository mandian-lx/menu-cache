%define git 0

Summary:	A library to speed up freedesktop.org application menus
Name:		menu-cache
Version:	1.0.2
%if %git
Source0:	%{name}-%{git}.tar.xz
Release:	0.%git.1
%else
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
Release:	6
%endif
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://github.com/lxde/menu-cache
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(libfm-extra)

%description
Lightweight X11 Desktop Environment project (a.k.a LXDE) aimed to provide a
new desktop environment which is useful enough and keep resource usage lower
at the same time. Useabiliy, speed, and memory usage are our main concern.

Unlike other tightly integrated desktops LXDE strives to be modular, so each
component can be used independently with few dependencies. This makes
porting LXDE to different distributions and platforms easier.

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

%define major 3
%define libname %mklibname %{name} %{major}

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		Graphical desktop/Other
Requires:	%{name} >= %{version}-%{release}

%description -n %{libname}
This package contains shared library for %{name}.

%files -n %{libname}
%{_libdir}/libmenu-cache.so.%{major}*

#----------------------------------------------------------------------

%define devname %mklibname -d %{name}

%package -n %{devname}
Summary:	Contains development files for %{name}
Group:		Graphical desktop/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains development files for %{name}.

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------
%prep
%if %{git}
%setup -qn %{name}-%{git}
%else
%setup -q
%endif
%apply_patches

[ -e autogen.sh ] && ./autogen.sh

%build
%configure
%make

%install
%makeinstall_std

