%global python3_pkgversion 3.11

%define  debug_package %{nil}
%define _prefix /opt/eda-rpm
%define _mandir %{_prefix}/share/man
%global __os_install_post %{nil}

%define service_user eda
%define service_group eda
%define service_homedir /var/lib/eda-rpm
%define service_logdir /var/log/eda-rpm
%define service_configdir /etc/eda-rpm

Summary: Ansible EDA-RPM (Event Driven Ansible Server)
Name: eda-rpm
Version: 2024.3.4
Release: 6%{dist}
Source0: eda-server-2024.3.4.tar.gz
#Source1: settings.py-%{version}
#Source2: awx-receiver.service-%{version}
#Source3: awx-dispatcher.service-%{version}
#Source4: awx-wsrelay.service-%{version}
#Source5: awx-ws-heartbeat.service-%{version}
#Source6: awx-daphne.service-%{version}
#Source7: awx-web.service-%{version}
#Source20: awx-receptor.service-%{version}
#Source21: awx-receptor-hop.service-%{version}
#Source22: awx-receptor-worker.service-%{version}
#Source23: awx.target-%{version}
#Source30: receptor.conf-%{version}
#Source31: receptor-hop.conf-%{version}
#Source32: receptor-worker.conf-%{version}
#Source40: awx-rpm-logo.svg-%{version}
#Source8: awx-rpm-nginx.conf-%{version}
#Patch0: awx-patch.patch-%{version}
License: GPLv3
Group: AWX
URL: https://awx.wiki
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: AWX
Prefix: %{_prefix}
AutoReqProv: false

BuildRequires: make python%{python3_pkgversion} python%{python3_pkgversion}-devel nodejs npm gettext git python%{python3_pkgversion}-build rsync libpq libpq-devel 
BuildRequires: python3.11-adal = 1.2.7
BuildRequires: python3.11-annotated-types = 0.6.0
BuildRequires: python3.11-asgiref = 3.7.2
BuildRequires: python3.11-async-timeout = 4.0.3
BuildRequires: python3.11-attrs = 23.2.0
BuildRequires: python3.11-autobahn = 23.6.2
BuildRequires: python3.11-automat = 22.10.0
BuildRequires: python3.11-babel = 2.15.0
BuildRequires: python3.11-bcrypt = 4.1.3
BuildRequires: python3.11-bcrypt+tests = 4.1.3
BuildRequires: python3.11-bcrypt+typecheck = 4.1.3
BuildRequires: python3.11-blinker = 1.8.2
BuildRequires: python3.11-build = 1.2.1
BuildRequires: python3.11-cachecontrol = 0.14.0
BuildRequires: python3.11-cachecontrol+filecache = 0.14.0
BuildRequires: python3.11-cachetools = 5.3.2
BuildRequires: python3.11-calver = 2022.6.26
BuildRequires: python3.11-certifi = 2023.7.22
BuildRequires: python3.11-cffi = 1.16.0
BuildRequires: python3.11-channels = 3.0.5
BuildRequires: python3.11-charset-normalizer = 3.3.2
BuildRequires: python3.11-cleo = 2.1.0
BuildRequires: python3.11-click = 8.1.7
BuildRequires: python3.11-colorama = 0.4.6
BuildRequires: python3.11-constantly = 23.10.4
BuildRequires: python3.11-crashtest = 0.4.1
BuildRequires: python3.11-croniter = 1.3.14
BuildRequires: python3.11-cryptography = 41.0.7
BuildRequires: python3.11-daphne = 3.0.2
BuildRequires: python3.11-defusedxml = 0.7.1
BuildRequires: python3.11-distlib = 0.3.8
BuildRequires: python3.11-distro = 1.9.0
BuildRequires: python3.11-django = 4.2.6
BuildRequires: python3.11-django-ansible-base = 20240423
BuildRequires: python3.11-django-ansible-base+jwt_consumer = 20240423
BuildRequires: python3.11-django-ansible-base+rest_filters = 20240423
BuildRequires: python3.11-django-auth-ldap = 4.8.0
BuildRequires: python3.11-django+bcrypt = 4.2.6
BuildRequires: python3.11-django-crum = 0.7.9
BuildRequires: python3.11-django-filter = 23.5
BuildRequires: python3.11-djangorestframework = 3.15.1
BuildRequires: python3.11-djangorestframework-simplejwt = 5.3.1
BuildRequires: python3.11-django-rq = 2.7.0
BuildRequires: python3.11-django-split-settings = 1.0.0
BuildRequires: python3.11-docutils = 0.20.1
BuildRequires: python3.11-drf-spectacular = 0.26.5
BuildRequires: python3.11-dulwich = 0.21.7
BuildRequires: python3.11-dynaconf = 3.2.4
BuildRequires: python3.11-ecdsa = 0.18.0
BuildRequires: python3.11-fastjsonschema = 2.19.1
BuildRequires: python3.11-filelock = 3.13.1
BuildRequires: python3.11-google-auth = 2.28.1
BuildRequires: python3.11-h2 = 4.1.0
BuildRequires: python3.11-hatch-fancy-pypi-readme = 24.1.0
BuildRequires: python3.11-hatchling = 1.24.2
BuildRequires: python3.11-hatch-vcs = 0.4.0
BuildRequires: python3.11-hpack = 4.0.0
BuildRequires: python3.11-hyperframe = 6.0.1
BuildRequires: python3.11-hyperlink = 21.0.0
BuildRequires: python3.11-idna = 3.6
BuildRequires: python3.11-importlib-metadata = 6.2.1
BuildRequires: python3.11-incremental = 22.10.0
BuildRequires: python3.11-inflection = 0.5.1
BuildRequires: python3.11-installer = 0.7.0
BuildRequires: python3.11-isodate = 0.6.1
BuildRequires: python3.11-jaraco-classes = 3.4.0
BuildRequires: python3.11-jeepney = 0.8.0
BuildRequires: python3.11-jinja2 = 3.1.3
BuildRequires: python3.11-jinja2+i18n = 3.1.3
BuildRequires: python3.11-jsonschema = 4.21.1
BuildRequires: python3.11-jsonschema-specifications = 2023.12.1
BuildRequires: python3.11-keyring = 24.3.1
BuildRequires: python3.11-kubernetes = 29.0.0
BuildRequires: python3.11-kubernetes+adal = 29.0.0
BuildRequires: python3.11-lxml = 4.9.4
BuildRequires: python3.11-markdown-it-py = 3.0.0
BuildRequires: python3.11-markupsafe = 2.1.5
BuildRequires: python3.11-maturin = 1.5.1
BuildRequires: python3.11-mdurl = 0.1.2
BuildRequires: python3.11-more-itertools = 10.2.0
BuildRequires: python3.11-msgpack = 1.0.5
BuildRequires: python3.11-mypy = 1.10.0
BuildRequires: python3.11-mypy-extensions = 1.0.0
BuildRequires: python3.11-nh3 = 0.2.17
BuildRequires: python3.11-oauthlib = 3.2.2
BuildRequires: python3.11-oauthlib+signedtoken = 3.2.2
BuildRequires: python3.11-packaging = 23.2
BuildRequires: python3.11-pathspec = 0.12.1
BuildRequires: python3.11-pexpect = 4.9.0
BuildRequires: python3.11-pkgconfig = 1.5.5
BuildRequires: python3.11-pkginfo = 1.10.0
BuildRequires: python3.11-platformdirs = 3.11.0
BuildRequires: python3.11-podman = 4.9.0
BuildRequires: python3.11-priority = 1.3.0
BuildRequires: python3.11-ptyprocess = 0.7.0
BuildRequires: python3.11-pyasn1-modules = 0.5.1
BuildRequires: python3.11-pycparser = 2.21
BuildRequires: python3.11-pydantic = 2.5.0
BuildRequires: python3.11-pydantic-core = 2.14.1
BuildRequires: python3.11-pygments = 2.18.0
BuildRequires: python3.11-pyhamcrest = 2.1.0
BuildRequires: python3.11-pyjwt = 2.8.0
BuildRequires: python3.11-pyjwt+crypto = 2.8.0
BuildRequires: python3.11-pyopenssl = 24.0.0
BuildRequires: python3.11-pyproject-hooks = 1.1.0
BuildRequires: python3.11-pyrsistent = 0.19.3
BuildRequires: python3.11-pytest-runner = 6.0.1
BuildRequires: python3.11-python3-openid = 3.2.0
BuildRequires: python3.11-python3-saml = 1.16.0
BuildRequires: python3.11-python-dateutil = 2.9.0^post0
BuildRequires: python3.11-python-jose = 3.3.0
BuildRequires: python3.11-python-ldap = 3.4.4
BuildRequires: python3.11-python-ntlm = 1.1.0
BuildRequires: python3.11-pytz = 2024.1
BuildRequires: python3.11-pyxdg = 0.28
BuildRequires: python3.11-pyyaml = 6.0.1
BuildRequires: python3.11-rapidfuzz = 3.9.1
BuildRequires: python3.11-readme-renderer = 43.0
BuildRequires: python3.11-redis = 5.0.1
BuildRequires: python3.11-referencing = 0.33.0
BuildRequires: python3.11-requests = 2.31.0
BuildRequires: python3.11-requests-oauthlib = 1.3.1
BuildRequires: python3.11-requests-oauthlib+rsa = 1.3.1
BuildRequires: python3.11-requests+socks = 2.31.0
BuildRequires: python3.11-requests-toolbelt = 1.0.0
BuildRequires: python3.11-rfc3986 = 2.0.0
BuildRequires: python3.11-rfc3986+idna2008 = 2.0.0
BuildRequires: python3.11-rich = 13.7.1
BuildRequires: python3.11-rpds-py = 0.18.0
BuildRequires: python3.11-rq = 1.13.0
BuildRequires: python3.11-rq-scheduler = 0.10.0
BuildRequires: python3.11-rsa = 4.9
BuildRequires: python3.11-scikit-build = 0.17.6
BuildRequires: python3.11-secretstorage = 3.3.3
BuildRequires: python3.11-service-identity = 24.1.0
BuildRequires: python3.11-setuptools = 69.0.2
BuildRequires: python3.11-setuptools_scm = 8.0.4
BuildRequires: python3.11-setuptools_scm+toml = 8.0.4
BuildRequires: python3.11-setuptools-twine = 0.1.3
BuildRequires: python3.11-shellingham = 1.5.4
BuildRequires: python3.11-six = 1.16.0
BuildRequires: python3.11-social-auth-app-django = 5.4.0
BuildRequires: python3.11-social-auth-core = 4.4.2
BuildRequires: python3.11-social-auth-core+all = 4.4.2
BuildRequires: python3.11-social-auth-core+allpy3 = 4.4.2
BuildRequires: python3.11-social-auth-core+azuread = 4.4.2
BuildRequires: python3.11-social-auth-core+openidconnect = 4.4.2
BuildRequires: python3.11-social-auth-core+saml = 4.4.2
BuildRequires: python3.11-sqlparse = 0.4.4
BuildRequires: python3.11-tabulate = 0.9.0
BuildRequires: python3.11-tomlkit = 0.12.5
BuildRequires: python3.11-trove-classifiers = 2024.5.22
BuildRequires: python3.11-twine = 5.1.0
BuildRequires: python3.11-twisted = 23.10.0
BuildRequires: python3.11-twisted+http2 = 23.10.0
BuildRequires: python3.11-twisted+tls = 23.10.0
BuildRequires: python3.11-txaio = 23.1.1
BuildRequires: python3.11-types-psutil = 5.9.5.20240516
BuildRequires: python3.11-types-setuptools = 69.5.0.20240522
BuildRequires: python3.11-typing-extensions = 4.9.0
BuildRequires: python3.11-tzdata = 2023.3
BuildRequires: python3.11-uritemplate = 4.1.1
BuildRequires: python3.11-urllib3 = 1.26.18
BuildRequires: python3.11-versioneer = 0.29
BuildRequires: python3.11-versioneer+toml = 0.29
BuildRequires: python3.11-virtualenv = 20.26.2
BuildRequires: python3.11-websocket-client = 1.7.0
BuildRequires: python3.11-xmlsec = 1.3.13
BuildRequires: python3.11-zipp = 3.17.0
BuildRequires: python3.11-zope-interface = 6.2
BuildRequires: python3.11-poetry
BuildRequires: python3.11-pyasn1 python3.11-pip 

Requires: python%{python3_pkgversion} nodejs >= 18 npm gettext git nginx redis xmlsec1-openssl xmlsec1 podman sscg awx-receptor libpq 
Requires: python3.11-adal = 1.2.7
Requires: python3.11-annotated-types = 0.6.0
Requires: python3.11-asgiref = 3.7.2
Requires: python3.11-async-timeout = 4.0.3
Requires: python3.11-attrs = 23.2.0
Requires: python3.11-autobahn = 23.6.2
Requires: python3.11-automat = 22.10.0
Requires: python3.11-babel = 2.15.0
Requires: python3.11-bcrypt = 4.1.3
Requires: python3.11-bcrypt+tests = 4.1.3
Requires: python3.11-bcrypt+typecheck = 4.1.3
Requires: python3.11-blinker = 1.8.2
Requires: python3.11-build = 1.2.1
Requires: python3.11-cachecontrol = 0.14.0
Requires: python3.11-cachecontrol+filecache = 0.14.0
Requires: python3.11-cachetools = 5.3.2
Requires: python3.11-calver = 2022.6.26
Requires: python3.11-certifi = 2023.7.22
Requires: python3.11-cffi = 1.16.0
Requires: python3.11-channels = 3.0.5
Requires: python3.11-charset-normalizer = 3.3.2
Requires: python3.11-cleo = 2.1.0
Requires: python3.11-click = 8.1.7
Requires: python3.11-colorama = 0.4.6
Requires: python3.11-constantly = 23.10.4
Requires: python3.11-crashtest = 0.4.1
Requires: python3.11-croniter = 1.3.14
Requires: python3.11-cryptography = 41.0.7
Requires: python3.11-daphne = 3.0.2
Requires: python3.11-defusedxml = 0.7.1
Requires: python3.11-distlib = 0.3.8
Requires: python3.11-distro = 1.9.0
Requires: python3.11-django = 4.2.6
Requires: python3.11-django-ansible-base = 20240423
Requires: python3.11-django-ansible-base+jwt_consumer = 20240423
Requires: python3.11-django-ansible-base+rest_filters = 20240423
Requires: python3.11-django-auth-ldap = 4.8.0
Requires: python3.11-django+bcrypt = 4.2.6
Requires: python3.11-django-crum = 0.7.9
Requires: python3.11-django-filter = 23.5
Requires: python3.11-djangorestframework = 3.15.1
Requires: python3.11-djangorestframework-simplejwt = 5.3.1
Requires: python3.11-django-rq = 2.7.0
Requires: python3.11-django-split-settings = 1.0.0
Requires: python3.11-docutils = 0.20.1
Requires: python3.11-drf-spectacular = 0.26.5
Requires: python3.11-dulwich = 0.21.7
Requires: python3.11-dynaconf = 3.2.4
Requires: python3.11-ecdsa = 0.18.0
Requires: python3.11-fastjsonschema = 2.19.1
Requires: python3.11-filelock = 3.13.1
Requires: python3.11-google-auth = 2.28.1
Requires: python3.11-h2 = 4.1.0
Requires: python3.11-hatch-fancy-pypi-readme = 24.1.0
Requires: python3.11-hatchling = 1.24.2
Requires: python3.11-hatch-vcs = 0.4.0
Requires: python3.11-hpack = 4.0.0
Requires: python3.11-hyperframe = 6.0.1
Requires: python3.11-hyperlink = 21.0.0
Requires: python3.11-idna = 3.6
Requires: python3.11-importlib-metadata = 6.2.1
Requires: python3.11-incremental = 22.10.0
Requires: python3.11-inflection = 0.5.1
Requires: python3.11-installer = 0.7.0
Requires: python3.11-isodate = 0.6.1
Requires: python3.11-jaraco-classes = 3.4.0
Requires: python3.11-jeepney = 0.8.0
Requires: python3.11-jinja2 = 3.1.3
Requires: python3.11-jinja2+i18n = 3.1.3
Requires: python3.11-jsonschema = 4.21.1
Requires: python3.11-jsonschema-specifications = 2023.12.1
Requires: python3.11-keyring = 24.3.1
Requires: python3.11-kubernetes = 29.0.0
Requires: python3.11-kubernetes+adal = 29.0.0
Requires: python3.11-lxml = 4.9.4
Requires: python3.11-markdown-it-py = 3.0.0
Requires: python3.11-markupsafe = 2.1.5
Requires: python3.11-maturin = 1.5.1
Requires: python3.11-mdurl = 0.1.2
Requires: python3.11-more-itertools = 10.2.0
Requires: python3.11-msgpack = 1.0.5
Requires: python3.11-mypy = 1.10.0
Requires: python3.11-mypy-extensions = 1.0.0
Requires: python3.11-nh3 = 0.2.17
Requires: python3.11-oauthlib = 3.2.2
Requires: python3.11-oauthlib+signedtoken = 3.2.2
Requires: python3.11-packaging = 23.2
Requires: python3.11-pathspec = 0.12.1
Requires: python3.11-pexpect = 4.9.0
Requires: python3.11-pkgconfig = 1.5.5
Requires: python3.11-pkginfo = 1.10.0
Requires: python3.11-platformdirs = 3.11.0
Requires: python3.11-podman = 4.9.0
Requires: python3.11-priority = 1.3.0
Requires: python3.11-ptyprocess = 0.7.0
Requires: python3.11-pyasn1-modules = 0.5.1
Requires: python3.11-pycparser = 2.21
Requires: python3.11-pydantic = 2.5.0
Requires: python3.11-pydantic-core = 2.14.1
Requires: python3.11-pygments = 2.18.0
Requires: python3.11-pyhamcrest = 2.1.0
Requires: python3.11-pyjwt = 2.8.0
Requires: python3.11-pyjwt+crypto = 2.8.0
Requires: python3.11-pyopenssl = 24.0.0
Requires: python3.11-pyproject-hooks = 1.1.0
Requires: python3.11-pyrsistent = 0.19.3
Requires: python3.11-pytest-runner = 6.0.1
Requires: python3.11-python3-openid = 3.2.0
Requires: python3.11-python3-saml = 1.16.0
Requires: python3.11-python-dateutil = 2.9.0^post0
Requires: python3.11-python-jose = 3.3.0
Requires: python3.11-python-ldap = 3.4.4
Requires: python3.11-python-ntlm = 1.1.0
Requires: python3.11-pytz = 2024.1
Requires: python3.11-pyxdg = 0.28
Requires: python3.11-pyyaml = 6.0.1
Requires: python3.11-rapidfuzz = 3.9.1
Requires: python3.11-readme-renderer = 43.0
Requires: python3.11-redis = 5.0.1
Requires: python3.11-referencing = 0.33.0
Requires: python3.11-requests = 2.31.0
Requires: python3.11-requests-oauthlib = 1.3.1
Requires: python3.11-requests-oauthlib+rsa = 1.3.1
Requires: python3.11-requests+socks = 2.31.0
Requires: python3.11-requests-toolbelt = 1.0.0
Requires: python3.11-rfc3986 = 2.0.0
Requires: python3.11-rfc3986+idna2008 = 2.0.0
Requires: python3.11-rich = 13.7.1
Requires: python3.11-rpds-py = 0.18.0
Requires: python3.11-rq = 1.13.0
Requires: python3.11-rq-scheduler = 0.10.0
Requires: python3.11-rsa = 4.9
Requires: python3.11-scikit-build = 0.17.6
Requires: python3.11-secretstorage = 3.3.3
Requires: python3.11-service-identity = 24.1.0
Requires: python3.11-setuptools = 69.0.2
Requires: python3.11-setuptools_scm = 8.0.4
Requires: python3.11-setuptools_scm+toml = 8.0.4
Requires: python3.11-setuptools-twine = 0.1.3
Requires: python3.11-shellingham = 1.5.4
Requires: python3.11-six = 1.16.0
Requires: python3.11-social-auth-app-django = 5.4.0
Requires: python3.11-social-auth-core = 4.4.2
Requires: python3.11-social-auth-core+all = 4.4.2
Requires: python3.11-social-auth-core+allpy3 = 4.4.2
Requires: python3.11-social-auth-core+azuread = 4.4.2
Requires: python3.11-social-auth-core+openidconnect = 4.4.2
Requires: python3.11-social-auth-core+saml = 4.4.2
Requires: python3.11-sqlparse = 0.4.4
Requires: python3.11-tabulate = 0.9.0
Requires: python3.11-tomlkit = 0.12.5
Requires: python3.11-trove-classifiers = 2024.5.22
Requires: python3.11-twine = 5.1.0
Requires: python3.11-twisted = 23.10.0
Requires: python3.11-twisted+http2 = 23.10.0
Requires: python3.11-twisted+tls = 23.10.0
Requires: python3.11-txaio = 23.1.1
Requires: python3.11-types-psutil = 5.9.5.20240516
Requires: python3.11-types-setuptools = 69.5.0.20240522
Requires: python3.11-typing-extensions = 4.9.0
Requires: python3.11-tzdata = 2023.3
Requires: python3.11-uritemplate = 4.1.1
Requires: python3.11-urllib3 = 1.26.18
Requires: python3.11-versioneer = 0.29
Requires: python3.11-versioneer+toml = 0.29
Requires: python3.11-virtualenv = 20.26.2
Requires: python3.11-websocket-client = 1.7.0
Requires: python3.11-xmlsec = 1.3.13
Requires: python3.11-zipp = 3.17.0
Requires: python3.11-zope-interface = 6.2
Requires: python3.11-pyasn1 python3.11-pip 

%{?systemd_requires}

%description
%{summary}

%prep
%setup -q -n eda-server
git checkout -f devel
git checkout -f %{version}
#%patch0 -p0

%build

%install
poetry install -E all --only-root

#cp %{_sourcedir}/awx-rpm-logo.svg-%{version} awx/ui_next/src/frontend/awx/main/awx-rpm-logo.svg
#sed -i "s/awx-logo.svg/awx-rpm-logo.svg/g" awx/ui_next/src/frontend/awx/main/AwxMasthead.tsx

mkdir -p /var/log/eda-rpm

rm -rf awx-*
pip%{python3_pkgversion} install --root=%{buildroot}/ .
popd
sed -i "s|/builddir.*.x86_64||g" $RPM_BUILD_ROOT/usr/bin/awx-manage
pushd %{buildroot}/usr/lib/python%{python3_pkgversion}/site-packages/
for i in `find -type f`; do
	sed -i "s|/builddir.*.x86_64||g" $i
done
popd

rsync -avr awx/ $RPM_BUILD_ROOT/opt/awx-rpm/awx/
cp -a /var/lib/awx/public/static /opt/awx-rpm/

mkdir -p $RPM_BUILD_ROOT/var/lib/awx/rsyslog
mkdir -p $RPM_BUILD_ROOT/var/lib/awx/projects
mkdir -p $RPM_BUILD_ROOT/var/lib/awx/job_status

# Collect django static
mkdir -p /var/log/tower/
mkdir -p %{buildroot}%{service_homedir}
mkdir -p %{buildroot}%{service_logdir}
mkdir -p %{buildroot}%{_prefix}/bin
mkdir -p %{buildroot}%{service_configdir}
echo %{version} > %{buildroot}%{service_homedir}/.tower_version

cp %{_sourcedir}/settings.py-%{version} %{buildroot}%{service_configdir}/settings.py
mkdir -p %{buildroot}%{_prefix}/public
rsync -avr /var/lib/awx/public/ %{buildroot}%{_prefix}/public/

mkdir -p %{buildroot}/usr/lib/systemd/system
# awx-channels-worker awx
for service in awx-web awx-wsrelay awx-ws-heartbeat awx-daphne awx-dispatcher awx-receiver awx-receptor awx-receptor-hop awx-receptor-worker; do
    cp %{_sourcedir}/${service}.service-%{version} %{buildroot}/usr/lib/systemd/system/${service}.service
done

cp %{_sourcedir}/awx.target-%{version} %{buildroot}/usr/lib/systemd/system/awx.target

mkdir -p %{buildroot}/etc/receptor

for receptor in receptor receptor-hop receptor-worker; do
	cp %{_sourcedir}/$receptor.conf-%{version} %{buildroot}/etc/receptor/$receptor.conf
done

mkdir -p %{buildroot}/etc/nginx/conf.d

cp %{_sourcedir}/awx-rpm-nginx.conf-%{version} %{buildroot}/etc/nginx/conf.d/awx-rpm.conf

# Create Virtualenv folder
mkdir -p %{buildroot}%{service_homedir}/venv

mkdir -p $RPM_BUILD_ROOT/etc/nginx/conf.d/

sed -i "s/supervisor_service_command(command='restart', service='awx-rsyslogd')//g" $RPM_BUILD_ROOT/usr/lib/python%{python3_pkgversion}/site-packages/awx/main/utils/external_logging.py

%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir %{service_homedir} -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}
/usr/bin/gpasswd -a awx redis

%post
if [ ! -f /etc/nginx/nginx.crt ];then
sscg -q --cert-file /etc/nginx/nginx.crt --cert-key-file /etc/nginx/nginx.key --ca-file /etc/nginx/ca.crt --lifetime 3650 --hostname $HOSTNAME --email root@$HOSTNAME
fi

%preun

%postun

%clean

%files
%defattr(0644, awx, awx, 0755)
%attr(0755, root, root) /usr/bin/awx-manage
%attr(0755, root, root) /usr/lib/systemd/system/*.service
%attr(0755, root, root) /usr/lib/python%{python3_pkgversion}/site-packages/awx*
%attr(0755, awx, awx) %{_prefix}
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}/venv
%{service_homedir}/.tower_version
%dir %attr(0770, %{service_user}, %{service_group}) %{service_logdir}
%config(noreplace) %{service_configdir}/settings.py
%config /etc/nginx/conf.d/awx-rpm.conf
/usr/lib/systemd/system/awx.target
/etc/receptor
#/usr/bin/ansible-tower-service
#/usr/bin/ansible-tower-setup
#/usr/bin/awx-python
#/usr/bin/failure-event-handler
#/usr/share/awx
#/usr/share/sosreport/sos/plugins/tower.py
#/var/lib/awx/favicon.ico
#/var/lib/awx/wsgi.py
/var/lib/awx/rsyslog
/var/lib/awx/projects
/var/lib/awx/job_status

%changelog
* Tue Jun 04 2024 12:37:12 PM CEST +0200 Martin Juhl <m@rtinjuhl.dk> 2024.3.4
- New version build: 2024.3.4

