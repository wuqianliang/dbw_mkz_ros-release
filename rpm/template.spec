Name:           ros-indigo-dbw-mkz
Version:        1.0.13
Release:        0%{?dist}
Summary:        ROS dbw_mkz package

Group:          Development/Libraries
License:        BSD
URL:            http://dataspeedinc.com
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-dbw-mkz-can
Requires:       ros-indigo-dbw-mkz-description
Requires:       ros-indigo-dbw-mkz-joystick-demo
Requires:       ros-indigo-dbw-mkz-msgs
Requires:       ros-indigo-dbw-mkz-twist-controller
BuildRequires:  ros-indigo-catkin

%description
Drive-by-wire interface to the Dataspeed Inc. Lincoln MKZ DBW kit

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Jun 13 2018 Kevin Hallenbeck <khallenbeck@dataspeedinc.com> - 1.0.13-0
- Autogenerated by Bloom

