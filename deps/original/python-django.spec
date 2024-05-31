
%global python3_pkgversion 3.11

Name:           python-django
Version:        4.2.6
Release:        %autorelease
Summary:        A high-level Python web framework that encourages rapid development and clean, pragmatic design.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://www.djangoproject.com/
Source:         %{pypi_source Django}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-django
Summary:        %{summary}

%description -n python%{python3_pkgversion}-django %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-django argon2,bcrypt


%prep
%autosetup -p1 -n Django-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x argon2,bcrypt


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-django -f %{pyproject_files}


%changelog
%autochangelog