Name:           ros-indigo-hector-worldmodel-msgs
Version:        0.3.2
Release:        0%{?dist}
Summary:        ROS hector_worldmodel_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hector_worldmodel_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-sensor-msgs

%description
hector_worldmodel_msgs is a message package to comes with the hector_worldmodel
stack. The messages can be used to send percepts from images
(hector_worldmodel_msgs/ImagePercept) or other sources
(hector_worldmodel_msgs/PosePercept) to the hector_object_tracker node. The
tracker publishes model updates as hector_worldmodel_msgs/Object messages and
latches the whole model state as a hector_worldmodel_msgs/ObjectModel message.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Sep 06 2014 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.2-0
- Autogenerated by Bloom

