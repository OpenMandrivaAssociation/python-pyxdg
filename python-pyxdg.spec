%define oname   pyxdg
%define version 0.19
%define release 1

Name:             python-pyxdg
Summary:          Python library to access freedesktop.org standards
Version:          %{version}
Release:          %{release}
BuildArch:        noarch
Source0:          http://www.freedesktop.org/~lanius/%{oname}-%{version}.tar.gz
URL:              http://www.freedesktop.org/Software/pyxdg
Group:            System/Libraries
License:          LGPLv2
BuildRequires:    python-devel
Provides:         pyxdg
Obsoletes:        pyxdg < 0.19-3

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
%setup -qn %{oname}-%{version}

%build
python setup.py build

%install
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc AUTHORS COPYING ChangeLog README TODO


%changelog
* Sat May 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.19-1
+ Revision: 796457
- imported package python-pyxdg

