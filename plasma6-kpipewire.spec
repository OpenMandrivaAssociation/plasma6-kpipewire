%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define uvlibname %mklibname KPipeWire
%define libname %mklibname KPipeWire-plasma6
%define uvdevname %mklibname KPipeWire -d
%define devname %mklibname KPipeWire-plasma6 -d
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: plasma6-kpipewire
Version: 6.1.3
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/plasma/kpipewire/-/archive/%{gitbranch}/kpipewire-%{gitbranchd}.tar.bz2#/kpipewire-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/kpipewire-%{version}.tar.xz
%endif
Summary: A set of convenient classes to use PipeWire in Qt projects
URL: https://invent.kde.org/plasma/kpipewire
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: gettext
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KWayland)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libva)
BuildRequires: pkgconfig(libva-drm)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pipewire-utils
BuildRequires: pipewire
Requires: pipewire-utils
Requires: %{libname} = %{EVRD}
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%patchlist

%description
A set of convenient classes to use PipeWire in Qt projects

%package -n %{libname}
Summary: A set of convenient classes to use PipeWire in Qt projects
Group: System/Libraries
Requires: %{name} = %{EVRD}
Obsoletes: %{uvlibname} > 5.240.0-0

%description -n %{libname}
A set of convenient classes to use PipeWire in Qt projects

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Obsoletes: %{uvdevname} > 5.240.0-0
Requires: pkgconfig(epoxy)

%description -n %{devname}
Development files (Headers etc.) for %{name}.

A set of convenient classes to use PipeWire in Qt projects

#find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kpipewire.*
%{_datadir}/qlogging-categories6/kpipewirerecord.*

%files -n %{devname}
%{_includedir}/KPipeWire
%{_libdir}/cmake/KPipeWire

%files -n %{libname}
%{_libdir}/libKPipeWire.so*
%{_libdir}/libKPipeWireDmaBuf.so*
%{_libdir}/libKPipeWireRecord.so*
%{_qtdir}/qml/org/kde/pipewire
