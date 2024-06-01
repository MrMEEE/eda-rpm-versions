
%global python3_pkgversion 3.11

Name:           python-referencing
Version:        0.33.0
Release:        %autorelease
Summary:        JSON Referencing + Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/python-jsonschema/referencing
Source:         %{pypi_source referencing}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'referencing' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-referencing
Summary:        %{summary}

%description -n python%{python3_pkgversion}-referencing %_description


%prep
%autosetup -p1 -n referencing-%{version}


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


%files -n python%{python3_pkgversion}-referencing -f %{pyproject_files}


%changelog
%autochangelog