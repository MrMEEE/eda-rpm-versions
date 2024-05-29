
%global python3_pkgversion 3.11

Name:           python-social-auth-core
Version:        4.5.1
Release:        %autorelease
Summary:        Python social authentication made simple.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/python-social-auth/social-core
Source:         %{pypi_source social-auth-core}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'social-auth-core' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-social-auth-core
Summary:        %{summary}

%description -n python%{python3_pkgversion}-social-auth-core %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-social-auth-core all,allpy3,azuread,saml


%prep
%autosetup -p1 -n social-auth-core-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,allpy3,azuread,saml


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-social-auth-core -f %{pyproject_files}


%changelog
%autochangelog