#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyblake2
Version  : 1.1.2
Release  : 5
URL      : https://files.pythonhosted.org/packages/a6/ea/559658f48713567276cabe1344a9ef918adcb34a9da417dbf0a2f7477d8e/pyblake2-1.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/a6/ea/559658f48713567276cabe1344a9ef918adcb34a9da417dbf0a2f7477d8e/pyblake2-1.1.2.tar.gz
Summary  : BLAKE2 hash function extension module
Group    : Development/Tools
License  : CC0-1.0
Requires: pyblake2-license = %{version}-%{release}
Requires: pyblake2-python = %{version}-%{release}
Requires: pyblake2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
pyblake2 â BLAKE2 hash function for Python
==========================================

%package license
Summary: license components for the pyblake2 package.
Group: Default

%description license
license components for the pyblake2 package.


%package python
Summary: python components for the pyblake2 package.
Group: Default
Requires: pyblake2-python3 = %{version}-%{release}

%description python
python components for the pyblake2 package.


%package python3
Summary: python3 components for the pyblake2 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyblake2 package.


%prep
%setup -q -n pyblake2-1.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551028055
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyblake2
cp COPYING %{buildroot}/usr/share/package-licenses/pyblake2/COPYING
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyblake2/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
