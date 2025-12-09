%define oname pyxdg

Name:		python-pyxdg
Summary:	Python library to access freedesktop.org standards
Version:	0.28
Release:	4
Group:		System/Libraries
License:	LGPLv2
URL:		https://www.freedesktop.org/Software/pyxdg
Source0:	https://github.com/takluyver/pyxdg/archive/refs/tags/rel-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python
BuildSystem:	python
%rename pyxdg
%rename python-xdg

%description
PyXDG is a python library to access freedesktop.org standards. 
Currently supported are:

	* Base Directory Specification Version 0.6 

	* Menu Specification Version 1.0 

	* Desktop Entry Specification Version 1.0 

	* Icon Theme Specification Version 0.8 

	* Recent File Spec 0.2 

	* Shared-MIME-Database Specification 0.13 

%files
%doc AUTHORS COPYING ChangeLog README TODO
%{py_puresitedir}/xdg
%{py_puresitedir}/pyxdg-%{version}-*.*-info
