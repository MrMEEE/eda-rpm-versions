
%global python3_pkgversion 3.11

Name:           python-autobahn
Version:        23.1.2
Release:        %autorelease
Summary:        WebSocket client & server library, WAMP real-time framework

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/crossbario/autobahn-python
Source:         %{pypi_source autobahn}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'autobahn' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-autobahn
Summary:        %{summary}

%description -n python%{python3_pkgversion}-autobahn %_description


%prep
%autosetup -p1 -n autobahn-%{version}


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


%files -n python%{python3_pkgversion}-autobahn -f %{pyproject_files}


%changelog
%autochangelog