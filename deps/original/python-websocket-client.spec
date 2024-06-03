
%global python3_pkgversion 3.11

Name:           python-websocket-client
Version:        1.5.1
Release:        %autorelease
Summary:        WebSocket client for Python with low level API options

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/websocket-client/websocket-client.git
Source:         %{pypi_source websocket-client}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'websocket-client' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-websocket-client
Summary:        %{summary}

%description -n python%{python3_pkgversion}-websocket-client %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-websocket-client docs,optional,test


%prep
%autosetup -p1 -n websocket-client-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,optional,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-websocket-client -f %{pyproject_files}


%changelog
%autochangelog