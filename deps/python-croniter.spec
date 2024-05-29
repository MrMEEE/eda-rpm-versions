
%global python3_pkgversion 3.11

Name:           python-croniter
Version:        1.3.14
Release:        %autorelease
Summary:        croniter provides iteration for datetime object with cron like format

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://github.com/kiorky/croniter
Source:         %{pypi_source croniter}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'croniter' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-croniter
Summary:        %{summary}

%description -n python%{python3_pkgversion}-croniter %_description


%prep
%autosetup -p1 -n croniter-%{version}


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


%files -n python%{python3_pkgversion}-croniter -f %{pyproject_files}


%changelog
%autochangelog