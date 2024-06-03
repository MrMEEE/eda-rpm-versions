
%global python3_pkgversion 3.11

Name:           python-adal
Version:        1.2.7
Release:        %autorelease
Summary:        Note: This library is already replaced by MSAL Python, available here: https://pypi.org/project/msal/ .ADAL Python remains available here as a legacy. The ADAL for Python library makes it easy for python application to authenticate to Azure Active Directory (AAD) in order to access AAD protected web resources.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/AzureAD/azure-activedirectory-library-for-python
Source:         %{pypi_source adal}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'adal' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-adal
Summary:        %{summary}

%description -n python%{python3_pkgversion}-adal %_description


%prep
%autosetup -p1 -n adal-%{version}


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


%files -n python%{python3_pkgversion}-adal -f %{pyproject_files}


%changelog
%autochangelog