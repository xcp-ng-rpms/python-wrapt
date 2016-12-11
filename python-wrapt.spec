# Created by pyp2rpm-1.1.1
%global sname wrapt

%if 0%{?fedora}
%global with_python3 1
%global with_docs 1
%endif

%{!?_licensedir: %global license %%doc}

Name:           python-%{sname}
Version:        1.10.8
Release:        3%{?dist}
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
%doc README.rst
%license LICENSE
%{python2_sitearch}/%{sname}
%{python2_sitearch}/%{sname}-%{version}-py?.?.egg-info

%if 0%{?with_docs}
%files doc
%doc docs/build/html
%endif

%if 0%{?with_python3}
%files -n python3-wrapt
%doc README.rst
%license LICENSE
%{python3_sitearch}/%{sname}
%{python3_sitearch}/%{sname}-%{version}-py?.?.egg-info
%endif

%changelog
* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.10.8-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.8-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Apr 15 2016 Kevin Fenzi <kevin@scrye.com> - 1.10.8-1
- Update to 1.10.8. Fixes bug #1325923

* Mon Apr 04 2016 Ralph Bean <rbean@redhat.com> - 1.10.7-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Jul 06 2015 Ralph Bean <rbean@redhat.com> - 1.10.5-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

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
