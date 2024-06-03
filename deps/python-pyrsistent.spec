
%global python3_pkgversion 3.11

Name:           python-pyrsistent
Version:        0.19.3
Release:        %autorelease
Summary:        Persistent/Functional/Immutable data structures

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/tobgu/pyrsistent/
Source:         %{pypi_source pyrsistent}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyrsistent' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pyrsistent
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pyrsistent %_description


%prep
%autosetup -p1 -n pyrsistent-%{version}


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


%files -n python%{python3_pkgversion}-pyrsistent -f %{pyproject_files}


%changelog
%autochangelog