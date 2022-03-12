%define oname pyxdg

Name:		python-pyxdg
Summary:	Python library to access freedesktop.org standards
Version:	0.25
Release:	3
Group:		System/Libraries
License:	LGPLv2
URL:		http://www.freedesktop.org/Software/pyxdg
Source0:	http://people.freedesktop.org/~takluyver/pyxdg-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
%rename pyxdg

%description
PyXDG is a python library to access freedesktop.org standards. 
Currently supported are:

	* Base Directory Specification Version 0.6 

	* Menu Specification Version 1.0 

	* Desktop Entry Specification Version 1.0 

	* Icon Theme Specification Version 0.8 

	* Recent File Spec 0.2 

	* Shared-MIME-Database Specification 0.13 

%prep
%autosetup -n %{oname}-%{version}

%build
%py_build

%install
%py_install -- --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc AUTHORS COPYING ChangeLog README TODO
