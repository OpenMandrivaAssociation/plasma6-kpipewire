%define libname %mklibname KPipeWire
%define devname %mklibname KPipeWire -d
%define git 20230518

Name: kf6-kpipewire
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/plasma/kpipewire/-/archive/master/kpipewire-master.tar.bz2#/kpipewire-%{git}.tar.bz2
Summary: A set of convenient classes to use PipeWire in Qt projects
URL: https://invent.kde.org/plasma/kpipewire
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
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
BuildRequires: cmake(KF6Wayland)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libva)
BuildRequires: pkgconfig(libva-drm)
Requires: %{libname} = %{EVRD}

%description
A set of convenient classes to use PipeWire in Qt projects

%package -n %{libname}
Summary: A set of convenient classes to use PipeWire in Qt projects
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
A set of convenient classes to use PipeWire in Qt projects

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

A set of convenient classes to use PipeWire in Qt projects

%prep
%autosetup -p1 -n kpipewire-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

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
