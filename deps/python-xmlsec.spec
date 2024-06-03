
%global python3_pkgversion 3.11

Name:           python-xmlsec
Version:        1.3.13
Release:        %autorelease
Summary:        Python bindings for the XML Security Library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/mehcode/python-xmlsec
Source:         %{pypi_source xmlsec}

BuildArch:      x86_64
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  gcc
BuildRequires:  xmlsec1-openssl
BuildRequires:  xmlsec1-nss
BuildRequires:  xmlsec1
BuildRequires:  xmlsec1-devel
BuildRequires:  libtool-ltdl-devel

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'xmlsec' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-xmlsec
Summary:        %{summary}

%description -n python%{python3_pkgversion}-xmlsec %_description


%prep
%autosetup -p1 -n xmlsec-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-xmlsec -f %{pyproject_files}


%changelog
%autochangelog