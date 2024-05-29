
%global python3_pkgversion 3.11

Name:           python-websocket-client
Version:        1.7.0
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


%prep
%autosetup -p1 -n websocket-client-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/wsdump $RPM_BUILD_ROOT/usr/bin/wsdump%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/wsdump|/usr/bin/wsdump%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-websocket-client -f %{pyproject_files}


%changelog
%autochangelog