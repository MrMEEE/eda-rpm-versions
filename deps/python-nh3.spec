%global debug_package %{nil}
%global python3_pkgversion 3.11

Name:           python-nh3
Version:        0.2.17
Release:        %autorelease
Summary:        Python bindings to the ammonia HTML sanitization library.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/nh3/
Source:         %{pypi_source nh3}

BuildArch:      x86_64
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  gcc
BuildRequires:  rust
BuildRequires:  cargo


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'nh3' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-nh3
Summary:        %{summary}

%description -n python%{python3_pkgversion}-nh3 %_description


%prep
%autosetup -p1 -n nh3-%{version}


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


%files -n python%{python3_pkgversion}-nh3 -f %{pyproject_files}


%changelog
%autochangelog