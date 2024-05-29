
%global python3_pkgversion 3.11

Name:           python-typing-extensions
Version:        4.9.0
Release:        %autorelease
Summary:        Backported and Experimental Type Hints for Python 3.8+

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/typing-extensions/
Source:         %{pypi_source typing_extensions}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'typing-extensions' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-typing-extensions
Summary:        %{summary}

%description -n python%{python3_pkgversion}-typing-extensions %_description


%prep
%autosetup -p1 -n typing_extensions-%{version}


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


%files -n python%{python3_pkgversion}-typing-extensions -f %{pyproject_files}


%changelog
%autochangelog