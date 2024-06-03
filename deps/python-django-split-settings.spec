
%global python3_pkgversion 3.11

Name:           python-django-split-settings
Version:        1.0.0
Release:        %autorelease
Summary:        Organize Django settings into multiple files and directories. Easily override and modify settings. Use wildcards and optional settings files.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://django-split-settings.readthedocs.io
Source:         %{pypi_source django-split-settings}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-split-settings' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-django-split-settings
Summary:        %{summary}

%description -n python%{python3_pkgversion}-django-split-settings %_description


%prep
%autosetup -p1 -n django-split-settings-%{version}


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


%files -n python%{python3_pkgversion}-django-split-settings -f %{pyproject_files}


%changelog
%autochangelog