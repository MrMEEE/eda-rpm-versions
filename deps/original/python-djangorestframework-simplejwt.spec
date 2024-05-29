
%global python3_pkgversion 3.11

Name:           python-djangorestframework-simplejwt
Version:        5.3.1
Release:        %autorelease
Summary:        A minimal JSON Web Token authentication plugin for Django REST Framework

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/jazzband/djangorestframework-simplejwt
Source:         %{pypi_source djangorestframework_simplejwt}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'djangorestframework-simplejwt' generated automatically by
pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-djangorestframework-simplejwt
Summary:        %{summary}

%description -n python%{python3_pkgversion}-djangorestframework-simplejwt %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-djangorestframework-simplejwt crypto,dev,doc,lint,python-jose,test


%prep
%autosetup -p1 -n djangorestframework_simplejwt-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x crypto,dev,doc,lint,python-jose,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-djangorestframework-simplejwt -f %{pyproject_files}


%changelog
%autochangelog