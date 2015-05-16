# Created by pyp2rpm-1.1.1
%global sname wrapt

%if 0%{?fedora}
%global with_python3 1
%global with_docs 1
%endif

%{!?_licensedir: %global license %%doc}

Name:           python-%{sname}
Version:        1.10.4
Release:        6%{?dist}
Summary:        A Python module for decorators, wrappers and monkey patching

License:        BSD
URL:            https://github.com/GrahamDumpleton/wrapt
Source0:        https://github.com/GrahamDumpleton/%{sname}/archive/%{version}.tar.gz

BuildRequires:  python2-devel

%if 0%{?with_python3}
BuildRequires:  python3-devel
%endif

%description
The aim of the wrapt module is to provide a transparent object proxy
for Python, which can be used as the basis for the construction of
function wrappers and decorator functions.

%if 0%{?with_docs}
%package doc
Summary:        Documentation for the wrapt module

BuildRequires:  python-sphinx
BuildRequires:  python-sphinx_rtd_theme

%description doc
Documentation for the wrapt module
%endif

%if 0%{?with_python3}
%package -n python3-wrapt
Summary:        A Python module for decorators, wrappers and monkey patching

%description -n python3-wrapt
The aim of the wrapt module is to provide a transparent object proxy
for Python, which can be used as the basis for the construction of
function wrappers and decorator functions.
%endif

%prep
%setup -q -n %{sname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{sname}.egg-info
%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd
%endif

%if 0%{?with_docs}
# for docs
pushd docs
sphinx-build -b html -d build/doctrees . build/html
popd
%endif

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README
%license LICENSE
%{python2_sitearch}/%{sname}
%{python2_sitearch}/%{sname}-%{version}-py?.?.egg-info

%if 0%{?with_docs}
%files doc
%doc docs/build/html
%endif

%if 0%{?with_python3}
%files -n python3-wrapt
%doc README
%license LICENSE
%{python3_sitearch}/%{sname}
%{python3_sitearch}/%{sname}-%{version}-py?.?.egg-info
%endif

%changelog
* Fri May 15 2015 Ralph Bean <rbean@redhat.com> - 1.10.4-6
- Don't build docs on epel7 (the rtd theme is problematic).

* Sat Apr 11 2015 Ralph Bean <rbean@redhat.com> - 1.10.4-5
- Add python3 subpackage

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
