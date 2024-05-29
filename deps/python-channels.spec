
%global python3_pkgversion 3.11

Name:           python-channels
Version:        3.0.5
Release:        %autorelease
Summary:        Brings async, event-driven capabilities to Django. Django 2.2 and up only.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://github.com/django/channels
Source:         %{pypi_source channels}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'channels' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-channels
Summary:        %{summary}

%description -n python%{python3_pkgversion}-channels %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n channels-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
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


%files -n python%{python3_pkgversion}-channels -f %{pyproject_files}


%changelog
%autochangelog