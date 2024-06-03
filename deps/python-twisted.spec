%bcond_without check
%global python3_pkgversion 3.11

Name:           python-twisted
Version:        23.10.0
Release:        %autorelease
Summary:        An asynchronous networking framework written in Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://twistedmatrix.com/
Source:         %{pypi_source twisted}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel python%{python3_pkgversion}-cryptography python%{python3_pkgversion}-bcrypt python%{python3_pkgversion}-pyasn1 python%{python3_pkgversion}-tkinter python%{python3_pkgversion}-pyhamcrest glibc-langpack-en python%{python3_pkgversion}-pyopenssl


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'twisted' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-twisted
Summary:        %{summary}

%description -n python%{python3_pkgversion}-twisted %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-twisted http2,tls


%prep
%autosetup -p1 -n twisted-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x http2,tls


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/cftp $RPM_BUILD_ROOT/usr/bin/cftp%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/ckeygen $RPM_BUILD_ROOT/usr/bin/ckeygen%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/conch $RPM_BUILD_ROOT/usr/bin/conch%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/mailmail $RPM_BUILD_ROOT/usr/bin/mailmail%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/pyhtmlizer $RPM_BUILD_ROOT/usr/bin/pyhtmlizer%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/tkconch $RPM_BUILD_ROOT/usr/bin/tkconch%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/trial $RPM_BUILD_ROOT/usr/bin/trial%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/twist $RPM_BUILD_ROOT/usr/bin/twist%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/twistd $RPM_BUILD_ROOT/usr/bin/twistd%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/cftp$|/usr/bin/cftp%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/ckeygen$|/usr/bin/ckeygen%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/conch$|/usr/bin/conch%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/mailmail$|/usr/bin/mailmail%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/pyhtmlizer$|/usr/bin/pyhtmlizer%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/tkconch$|/usr/bin/tkconch%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/trial$|/usr/bin/trial%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/twist$|/usr/bin/twist%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/twistd$|/usr/bin/twistd%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-twisted -f %{pyproject_files}


%changelog
%autochangelog