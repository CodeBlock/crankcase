%global cartridgedir %{_libexecdir}/stickshift/cartridges/python-2.6

Summary:   Provides python-2.6 support
Name:      cartridge-python-2.6
Version: 0.96.3
Release:   1%{?dist}
Group:     Development/Languages
License:   ASL 2.0
URL:       http://openshift.redhat.com
Source0: http://mirror.openshift.com/pub/crankcase/source/%{name}/%{name}-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: git
Requires:  stickshift-abstract
Requires:  rubygem(stickshift-node)
Requires:  mod_bw
Requires:  python
Requires:  mod_wsgi >= 3.2
Requires:  MySQL-python
Requires:  pymongo
Requires:  pymongo-gridfs
Requires:  python-psycopg2
Requires:  python-virtualenv
Requires:  python-magic
Requires:  libjpeg
Requires:  libjpeg-devel
Requires:  libcurl
Requires:  libcurl-devel
Requires:  numpy
Requires:  numpy-f2py
Requires:  gcc-gfortran
Requires:  freetype-devel

Obsoletes: cartridge-python-3.2

BuildArch: noarch

%description
Provides wsgi support to OpenShift

%prep
%setup -q

%build
rm -rf git_template
cp -r template/ git_template/
cd git_template
git init
git add -f .
git config user.email "builder@example.com"
git config user.name "Template builder"
git commit -m 'Creating template'
cd ..
git clone --bare git_template git_template.git
rm -rf git_template
touch git_template.git/refs/heads/.gitignore

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{cartridgedir}
mkdir -p %{buildroot}/%{_sysconfdir}/stickshift/cartridges
ln -s %{cartridgedir}/info/configuration/ %{buildroot}/%{_sysconfdir}/stickshift/cartridges/%{name}
cp -r info %{buildroot}%{cartridgedir}/
cp LICENSE %{buildroot}%{cartridgedir}/
cp COPYRIGHT %{buildroot}%{cartridgedir}/
mkdir -p %{buildroot}%{cartridgedir}/info/data/
cp -r git_template.git %{buildroot}%{cartridgedir}/info/data/
ln -s %{cartridgedir}/../abstract/info/hooks/add-module %{buildroot}%{cartridgedir}/info/hooks/add-module
ln -s %{cartridgedir}/../abstract/info/hooks/info %{buildroot}%{cartridgedir}/info/hooks/info
ln -s %{cartridgedir}/../abstract/info/hooks/post-install %{buildroot}%{cartridgedir}/info/hooks/post-install
ln -s %{cartridgedir}/../abstract/info/hooks/post-remove %{buildroot}%{cartridgedir}/info/hooks/post-remove
ln -s %{cartridgedir}/../abstract/info/hooks/reload %{buildroot}%{cartridgedir}/info/hooks/reload
ln -s %{cartridgedir}/../abstract/info/hooks/remove-module %{buildroot}%{cartridgedir}/info/hooks/remove-module
ln -s %{cartridgedir}/../abstract/info/hooks/restart %{buildroot}%{cartridgedir}/info/hooks/restart
ln -s %{cartridgedir}/../abstract/info/hooks/start %{buildroot}%{cartridgedir}/info/hooks/start
ln -s %{cartridgedir}/../abstract-httpd/info/hooks/status %{buildroot}%{cartridgedir}/info/hooks/status
ln -s %{cartridgedir}/../abstract/info/hooks/stop %{buildroot}%{cartridgedir}/info/hooks/stop
ln -s %{cartridgedir}/../abstract/info/hooks/update-namespace %{buildroot}%{cartridgedir}/info/hooks/update-namespace
ln -s %{cartridgedir}/../abstract/info/hooks/deploy-httpd-proxy %{buildroot}%{cartridgedir}/info/hooks/deploy-httpd-proxy
ln -s %{cartridgedir}/../abstract/info/hooks/remove-httpd-proxy %{buildroot}%{cartridgedir}/info/hooks/remove-httpd-proxy
ln -s %{cartridgedir}/../abstract/info/hooks/force-stop %{buildroot}%{cartridgedir}/info/hooks/force-stop
ln -s %{cartridgedir}/../abstract/info/hooks/add-alias %{buildroot}%{cartridgedir}/info/hooks/add-alias
ln -s %{cartridgedir}/../abstract/info/hooks/tidy %{buildroot}%{cartridgedir}/info/hooks/tidy
ln -s %{cartridgedir}/../abstract/info/hooks/remove-alias %{buildroot}%{cartridgedir}/info/hooks/remove-alias
ln -s %{cartridgedir}/../abstract/info/hooks/move %{buildroot}%{cartridgedir}/info/hooks/move
ln -s %{cartridgedir}/../abstract/info/hooks/threaddump %{buildroot}%{cartridgedir}/info/hooks/threaddump
ln -s %{cartridgedir}/../abstract/info/hooks/expose-port %{buildroot}%{cartridgedir}/info/hooks/expose-port
ln -s %{cartridgedir}/../abstract/info/hooks/conceal-port %{buildroot}%{cartridgedir}/info/hooks/conceal-port
ln -s %{cartridgedir}/../abstract/info/hooks/show-port %{buildroot}%{cartridgedir}/info/hooks/show-port
ln -s %{cartridgedir}/../abstract/info/hooks/system-messages %{buildroot}%{cartridgedir}/info/hooks/system-messages
mkdir -p %{buildroot}%{cartridgedir}/info/connection-hooks/
ln -s %{cartridgedir}/../abstract/info/connection-hooks/publish-gear-endpoint %{buildroot}%{cartridgedir}/info/connection-hooks/publish-gear-endpoint
ln -s %{cartridgedir}/../abstract/info/connection-hooks/publish-http-url %{buildroot}%{cartridgedir}/info/connection-hooks/publish-http-url
ln -s %{cartridgedir}/../abstract/info/connection-hooks/set-db-connection-info %{buildroot}%{cartridgedir}/info/connection-hooks/set-db-connection-info
ln -s %{cartridgedir}/../abstract/info/connection-hooks/set-nosql-db-connection-info %{buildroot}%{cartridgedir}/info/connection-hooks/set-nosql-db-connection-info
ln -s %{cartridgedir}/../abstract/info/bin/sync_gears.sh %{buildroot}%{cartridgedir}/info/bin/sync_gears.sh

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{cartridgedir}
%dir %{cartridgedir}/info/
%attr(0750,-,-) %{cartridgedir}/info/hooks/
%attr(0750,-,-) %{cartridgedir}/info/data/
%attr(0750,-,-) %{cartridgedir}/info/build/
%attr(0755,-,-) %{cartridgedir}/info/bin/
%attr(0755,-,-) %{cartridgedir}/info/connection-hooks/
%config(noreplace) %{cartridgedir}/info/configuration/
%{_sysconfdir}/stickshift/cartridges/%{name}
%{cartridgedir}/info/changelog
%{cartridgedir}/info/control
%{cartridgedir}/info/manifest.yml
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Tue Jul 24 2012 Adam Miller <admiller@redhat.com> 0.96.3-1
- Add pre and post destroy calls on gear destruction and move unobfuscate and
  stickshift-proxy out of cartridge hooks and into node. (rmillner@redhat.com)

* Thu Jul 19 2012 Adam Miller <admiller@redhat.com> 0.96.2-1
- Fix for bugz 840165 - update readmes. (ramr@redhat.com)
- Fixes for bugz 840030 - Apache blocks access to /icons. Remove these as
  mod_autoindex has now been turned OFF (see bugz 785050 for more details).
  (ramr@redhat.com)

* Wed Jul 11 2012 Adam Miller <admiller@redhat.com> 0.96.1-1
- bump_minor_versions for sprint 15 (admiller@redhat.com)

* Thu Jul 05 2012 Adam Miller <admiller@redhat.com> 0.95.2-1
- more cartridges have better metadata (rchopra@redhat.com)
- cart metadata work merged; depends service added; cartridges enhanced; unit
  tests updated (rchopra@redhat.com)

* Wed Jun 20 2012 Adam Miller <admiller@redhat.com> 0.95.1-1
- bump_minor_versions for sprint 14 (admiller@redhat.com)

* Fri Jun 15 2012 Adam Miller <admiller@redhat.com> 0.94.3-1
- Security - BZ785050 remove mod_autoindex from all httpd.confs
  (tkramer@redhat.com)

* Fri Jun 15 2012 Tim Kramer <tkramer@redhat.com>
- Security - BZ785050 removed mod_autoindex from both httpd.conf files (tkramer@redhat.com)

* Fri Jun 08 2012 Adam Miller <admiller@redhat.com> 0.94.2-1
- Fix for bugz 827827. Use freetype-devel (as that's available on rhel-6.2).
  (ramr@redhat.com)

* Fri Jun 01 2012 Adam Miller <admiller@redhat.com> 0.94.1-1
- bumping spec versions (admiller@redhat.com)

* Wed May 30 2012 Adam Miller <admiller@redhat.com> 0.93.7-1
- Bug 825354 (dmcphers@redhat.com)
- Adding a dependency resolution step (using post-recieve hook) for all
  applications created from templates. Simplifies workflow by not requiring an
  additional git pull/push step Cucumber tests (kraman@gmail.com)

* Fri May 25 2012 Adam Miller <admiller@redhat.com> 0.93.6-1
- Add numpy, numpy-f2py and gcc-gfortran for scientific py libraries support.
  (ramr@redhat.com)

* Thu May 24 2012 Adam Miller <admiller@redhat.com> 0.93.5-1
- disabling cgroups for deconfigure and configure events (mmcgrath@redhat.com)

* Tue May 22 2012 Dan McPherson <dmcphers@redhat.com> 0.93.4-1
- Merge branch 'master' of github.com:openshift/crankcase (rmillner@redhat.com)
- Merge branch 'master' into US2109 (rmillner@redhat.com)
- Automatic commit of package [cartridge-python-2.6] release [0.93.2-1].
  (admiller@redhat.com)
- remove preconfigure and more work making tests faster (dmcphers@redhat.com)
- Merge branch 'master' into US2109 (jhonce@redhat.com)
- Revert to cartridge type -- no app types any more. (ramr@redhat.com)
- Merge branch 'master' into US2109 (jhonce@redhat.com)
- Merge branch 'master' into US2109 (ramr@redhat.com)
- Use a utility function to remove the cartridge instance dir.
  (ramr@redhat.com)
- Bug fixes to get tests running - mysql and python fixes, delete user dirs
  otherwise rhc-accept-node fails and tests fail. (ramr@redhat.com)
- Cleanup and restore custom env vars support and fixup permissions.
  (ramr@redhat.com)
- Automatic commit of package [cartridge-python-2.6] release [0.92.5-1].
  (admiller@redhat.com)
- Merge branch 'master' into US2109 (ramr@redhat.com)
- Add and use cartridge instance specific functions. (ramr@redhat.com)
- Change to use cartridge instance dir in lieu of app_dir and correct use of
  app and $gear-name directories. (ramr@redhat.com)
- Merge branch 'master' into US2109 (ramr@redhat.com)

* Tue May 22 2012 Adam Miller <admiller@redhat.com> 0.93.3-1
- Changes to descriptors/specs to execute the new connector.
  (mpatel@redhat.com)

* Thu May 17 2012 Adam Miller <admiller@redhat.com> 0.93.2-1
- remove preconfigure and more work making tests faster (dmcphers@redhat.com)
- Adding python-magic as a req for bz 813700 (mmcgrath@redhat.com)
- Add sample user pre/post hooks. (rmillner@redhat.com)

* Thu May 10 2012 Adam Miller <admiller@redhat.com> 0.93.1-1
- bumping spec versions (admiller@redhat.com)

* Tue May 08 2012 Adam Miller <admiller@redhat.com> 0.92.5-1
- Bug 819739 (dmcphers@redhat.com)

* Mon May 07 2012 Adam Miller <admiller@redhat.com> 0.92.4-1
- Add support for pre/post start/stop hooks to both web application service and
  embedded cartridges.   Include the cartridge name in the calling hook to
  avoid conflicts when typeless gears are implemented. (rmillner@redhat.com)
- changed git config within spec files to operate on local repo instead of
  changing global values (kraman@gmail.com)

* Thu May 03 2012 Dan McPherson <dmcphers@redhat.com> 0.92.3-1
- Adding obsoletes for machines that may have cartridge with old name already
  installed. (kraman@gmail.com)

* Wed May 02 2012 Krishna Raman <kraman@gmail.com> 0.92.2-1
- new package built with tito

* Thu Apr 26 2012 Adam Miller <admiller@redhat.com> 0.92.1-1
- bumping spec versions (admiller@redhat.com)

* Wed Apr 25 2012 Krishna Raman <kraman@gmail.com> 0.91.7-1
- Update to python cartridge to use default (empty) mirror in Fedora
-  (kraman@gmail.com)

* Mon Apr 23 2012 Adam Miller <admiller@redhat.com> 0.91.6-1
- cleaning up spec files (dmcphers@redhat.com)
- Add system site packages to the virtual environment. Allows packages with
  custom build configurations like pycurl to be installed on the system via RPM
  and re-used rather than have to hack up per-package builds.  And faster to
  deploy. (rmillner@redhat.com)

* Sat Apr 21 2012 Dan McPherson <dmcphers@redhat.com> 0.91.5-1
- new package built with tito
