
%global python3_pkgversion 3.11

Name:           python-hatchling
Version:        1.24.2
Release:        %autorelease
Summary:        Modern, extensible Python build backend

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://hatch.pypa.io/latest/
Source:         %{pypi_source hatchling}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'hatchling' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-hatchling
Summary:        %{summary}

%description -n python%{python3_pkgversion}-hatchling %_description


%prep
%autosetup -p1 -n hatchling-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/hatchling $RPM_BUILD_ROOT/usr/bin/hatchling%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/hatchling|/usr/bin/hatchling%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-hatchling -f %{pyproject_files}


%changelog
%autochangelog