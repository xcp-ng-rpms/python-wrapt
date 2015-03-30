# Created by pyp2rpm-1.1.1
%global sname wrapt

Name:           python-%{sname}
Version:        1.10.4
Release:        4%{?dist}
Summary:        A Python module for decorators, wrappers and monkey patching

License:        BSD
URL:            https://github.com/GrahamDumpleton/wrapt
Source0:        https://github.com/GrahamDumpleton/%{sname}/archive/%{version}.tar.gz

BuildRequires:  python2-devel

%description
The aim of the wrapt module is to provide a transparent object proxy
for Python, which can be used as the basis for the construction of
function wrappers and decorator functions.

%package doc
Summary:        Documentation for the wrapt module

BuildRequires:  python-sphinx
BuildRequires:  python-sphinx_rtd_theme

%description doc
Documentation for the wrapt module

%prep
%setup -q -n %{sname}-%{version}

%build
%{__python2} setup.py build
# for docs
pushd docs
sphinx-build -b html -d build/doctrees . build/html
popd

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README
%license LICENSE
%{python2_sitearch}/%{sname}
%{python2_sitearch}/%{sname}-%{version}-py?.?.egg-info

%files doc
%doc docs/build/html

%changelog
* Wed Mar 25 2015 Chandan Kumar <chkumar246@gmail.com> - 1.10.4-4
- Added doc files for doc subpackage

* Wed Mar 25 2015 Chandan Kumar <chkumar246@gmail.com> - 1.10.4-3
- Fixed Docs

* Tue Mar 24 2015 Chandan Kumar <chkumar246@gmail.com> - 1.10.4-2
- Removed cflags and group section fro doc subpackage

* Tue Mar 24 2015 Chandan Kumar <chkumar246@gmail.com> - 1.10.4-1
- Bumped to upstream version 1.10.4
- Add docs

* Wed Mar 11 2015 Chandan Kumar <chkumar246@gmail.com> - 1.10.2-1
- Initial package.
