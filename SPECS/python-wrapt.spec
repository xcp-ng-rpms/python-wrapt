%global package_speccommit 26c7ee6610bc1d252a2f65a08688f42319df80de
%global usver 1.14.0
%global xsver 4
%global xsrel %{xsver}%{?xscount}%{?xshash}

%global sname wrapt

%global with_docs 0

%{!?_licensedir: %global license %%doc}

Name:           python-%{sname}
Version:        1.14.0
Release:        %{?xsrel}%{?dist}
Summary:        A Python module for decorators, wrappers and monkey patching

License:        BSD
URL:            https://github.com/GrahamDumpleton/wrapt
Source0: 1.14.0.tar.gz

BuildRequires:  gcc

BuildRequires:  python3-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%global _description %{expand:
The aim of the wrapt module is to provide a transparent object proxy
for Python, which can be used as the basis for the construction of
function wrappers and decorator functions.}

%description %_description

%if 0%{?with_docs}
%package doc
Summary:        Documentation for the wrapt module

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description doc
Documentation for the wrapt module
%endif

%package -n python3-wrapt
Summary:        A Python module for decorators, wrappers and monkey patching
%{?python_provide:%python_provide python3-wrapt}

%description -n python3-wrapt
The aim of the wrapt module is to provide a transparent object proxy
for Python, which can be used as the basis for the construction of
function wrappers and decorator functions.

%prep
%setup -q -n %{sname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{sname}.egg-info

%build
%py3_build

%if 0%{?with_docs}
# for docs
pushd docs
sphinx-build -b html -d build/doctrees . build/html
popd
%endif

%install
%py3_install

%if 0%{?with_docs}
%files doc
%doc docs/build/html
%endif

%files -n python3-wrapt
%doc README.rst
%license LICENSE
%{python3_sitearch}/%{sname}
%{python3_sitearch}/%{sname}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Aug 19 2024 Marcus Granado <marcus.granado@cloud.com> - 1.14.0-4
- Bump release and rebuild

* Fri Aug 09 2024 Marcus Granado <marcus.granado@cloud.com> - 1.14.0-3
- Bump release and rebuild

* Thu Jul 06 2023 Lin Liu <lin.liu@citrix.com> - 1.14.0-1
- First imported release

