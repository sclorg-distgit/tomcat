%global pkg_name tomcat
%{?scl:%scl_package %{pkg_name}}
%{?java_common_find_provides_and_requires}

# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%bcond_with lib

%global jspspec 2.2
%global major_version 7
%global minor_version 0
%global micro_version 42
%global packdname apache-tomcat-%{version}-src
%global servletspec 3.0
%global elspec 2.2
%global tcuid 91

# FHS 2.3 compliant tree structure - http://www.pathname.com/fhs/2.3/
%global libdir %{_javadir}/%{pkg_name}

Name:          %{?scl_prefix}%{pkg_name}
Epoch:         0
Version:       %{major_version}.%{minor_version}.%{micro_version}
Release:       1.21%{?dist}
Summary:       Apache Servlet/JSP Engine, RI for Servlet %{servletspec}/JSP %{jspspec} API

License:       ASL 2.0
URL:           http://tomcat.apache.org/
Source0:       http://www.apache.org/dist/tomcat/tomcat-%{major_version}/v%{version}/src/%{packdname}.tar.gz
Source1:       %{pkg_name}-%{major_version}.%{minor_version}.conf
Source2:       %{pkg_name}-%{major_version}.%{minor_version}.init
Source3:       %{pkg_name}-%{major_version}.%{minor_version}.sysconfig
Source4:       %{pkg_name}-%{major_version}.%{minor_version}.wrapper
Source5:       %{pkg_name}-%{major_version}.%{minor_version}.logrotate
Source6:       %{pkg_name}-%{major_version}.%{minor_version}-digest.script
Source7:       %{pkg_name}-%{major_version}.%{minor_version}-tool-wrapper.script
Source8:       servlet-api-OSGi-MANIFEST.MF
Source9:       jsp-api-OSGi-MANIFEST.MF
Source10:      %{pkg_name}-%{major_version}.%{minor_version}-log4j.properties
Source11:      %{pkg_name}-%{major_version}.%{minor_version}.service
Source12:      el-api-OSGi-MANIFEST.MF
Source13:      jasper-el-OSGi-MANIFEST.MF
Source14:      jasper-OSGi-MANIFEST.MF
Source15:      tomcat-api-OSGi-MANIFEST.MF
Source16:      tomcat-juli-OSGi-MANIFEST.MF
Source17:      %{pkg_name}-%{major_version}.%{minor_version}-tomcat-sysd
Source18:      %{pkg_name}-%{major_version}.%{minor_version}-tomcat-jsvc-sysd
Source19:      %{pkg_name}-%{major_version}.%{minor_version}-jsvc.wrapper
Source20:      %{pkg_name}-%{major_version}.%{minor_version}-jsvc.service


Patch0:        %{pkg_name}-%{major_version}.%{minor_version}-bootstrap-MANIFEST.MF.patch
Patch1:        %{pkg_name}-%{major_version}.%{minor_version}-tomcat-users-webapp.patch

BuildArch:     noarch

BuildRequires: %{?scl_prefix}ant
#BuildRequires: ant-nodeps
BuildRequires: %{?scl_prefix}ecj >= 1:4.2.1
BuildRequires: findutils
BuildRequires: %{?scl_prefix}apache-commons-collections
BuildRequires: %{?scl_prefix_maven}apache-commons-daemon
BuildRequires: %{?scl_prefix}apache-commons-dbcp
BuildRequires: %{?scl_prefix}apache-commons-pool
BuildRequires: %{?scl_prefix}jakarta-taglibs-standard
BuildRequires: %{?scl_prefix}javapackages-tools
BuildRequires: %{?scl_prefix}junit
BuildRequires: %{?scl_prefix}log4j
BuildRequires: %{?scl_prefix_maven}geronimo-jaxrpc
BuildRequires: %{?scl_prefix_maven}wsdl4j
BuildRequires: zip
Requires:      %{?scl_prefix_maven}apache-commons-daemon
Requires:      %{?scl_prefix}apache-commons-logging
Requires:      %{?scl_prefix}apache-commons-collections
Requires:      %{?scl_prefix}apache-commons-dbcp
Requires:      %{?scl_prefix}apache-commons-pool
Requires:      procps
Requires:      %{name}-lib = %{epoch}:%{version}-%{release}

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License version 2.0. Tomcat is intended
to be a collaboration of the best-of-breed developers from around the world.


%package javadoc
Summary: Javadoc generated documentation for Apache Tomcat

%description javadoc
Javadoc generated documentation for Apache Tomcat.

%package jsp-%{jspspec}-api
Summary: Apache Tomcat JSP API implementation classes
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}

%description jsp-%{jspspec}-api
Apache Tomcat JSP API implementation classes.

%if %{with lib}
%package lib
Summary: Libraries needed to run the Tomcat Web container
Requires: %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-el-%{elspec}-api = %{epoch}:%{version}-%{release}
Requires: %{?scl_prefix}ecj >= 1:4.2.1
Requires: %{?scl_prefix}apache-commons-collections
Requires: %{?scl_prefix}apache-commons-dbcp
Requires: %{?scl_prefix}apache-commons-pool
Requires(preun): coreutils

%description lib
Libraries needed to run the Tomcat Web container.
%endif

%package servlet-%{servletspec}-api
Summary: Apache Tomcat Servlet API implementation classes
Obsoletes: %{name}-lib < 0:7.0.42-1.21

%description servlet-%{servletspec}-api
Apache Tomcat Servlet API implementation classes.

%package el-%{elspec}-api
Summary: Expression Language v1.0 API
Obsoletes: %{name}-lib < 0:7.0.42-1.21

%description el-%{elspec}-api
Expression Language 1.0.

%prep
%setup -q -n %{packdname}
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
# remove pre-built binaries and windows files
find . -type f \( -name "*.bat" -o -name "*.class" -o -name Thumbs.db -o -name "*.gz" -o \
   -name "*.jar" -o -name "*.war" -o -name "*.zip" \) -delete

%patch0 -p0
%patch1 -p0
%{__ln_s} $(build-classpath jakarta-taglibs-core) webapps/examples/WEB-INF/lib/jstl.jar
%{__ln_s} $(build-classpath jakarta-taglibs-standard) webapps/examples/WEB-INF/lib/standard.jar
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
export OPT_JAR_LIST="xalan-j2-serializer"
   # we don't care about the tarballs and we're going to replace
   # tomcat-dbcp.jar with apache-commons-{collections,dbcp,pool}-tomcat5.jar
   # so just create a dummy file for later removal
   touch HACK
   %{__mkdir_p} HACKDIR
   touch HACKDIR/build.xml
   # who needs a build.properties file anyway
   %{ant} -Dbase.path="." \
      -Dbuild.compiler="modern" \
      -Dcommons-collections.jar="$(build-classpath apache-commons-collections)" \
      -Dcommons-daemon.jar="$(build-classpath apache-commons-daemon)" \
      -Dcommons-daemon.native.src.tgz="HACK" \
      -Djasper-jdt.jar="$(build-classpath ecj)" \
      -Djdt.jar="$(build-classpath ecj)" \
      -Dtomcat-dbcp.jar="$(build-classpath apache-commons-dbcp)" \
      -Dtomcat-native.tar.gz="HACK" \
      -Dtomcat-native.home="." \
      -Dcommons-daemon.native.win.mgr.exe="HACK" \
      -Dnsis.exe="HACK" \
      -Djaxrpc-lib.jar="$(build-classpath jaxrpc)" \
      -Dwsdl4j-lib.jar="$(build-classpath wsdl4j)" \
      -Dcommons-pool.home="HACKDIR" \
      -Dcommons-dbcp.home="HACKDIR" \
      -Dno.build.dbcp=true \
      -Dversion="%{version}" \
      -Dversion.build="%{micro_version}" \
      deploy dist-prepare dist-source javadoc

    # remove some jars that we'll replace with symlinks later
   %{__rm} output/build/bin/commons-daemon.jar \
           output/build/lib/ecj.jar \
           output/build/lib/apache-commons-dbcp.jar

    # remove the cruft we created
   %{__rm} output/build/bin/tomcat-native.tar.gz
pushd output/dist/src/webapps/docs/appdev/sample/src
%{__mkdir_p} ../web/WEB-INF/classes
/usr/bin/javac -cp ../../../../../../../../output/build/lib/servlet-api.jar -d ../web/WEB-INF/classes mypackage/Hello.java
pushd ../web
/usr/bin/jar cf ../../../../../../../../output/build/webapps/docs/appdev/sample/sample.war *
popd
popd

# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE8} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/servlet-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE9} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/jsp-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE12} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/el-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE13} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/jasper-el.jar META-INF/MANIFEST.MF
cp -p %{SOURCE14} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/jasper.jar META-INF/MANIFEST.MF
cp -p %{SOURCE15} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/tomcat-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE16} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/bin/tomcat-juli.jar META-INF/MANIFEST.MF
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x

%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_javadocdir}/%{pkg_name}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{libdir}

# move things into place
# First copy supporting libs to tomcat lib
pushd output/build
    %{__cp} -a bin/tomcat-juli.jar ${RPM_BUILD_ROOT}%{libdir}
    %{__cp} -a lib/*.jar ${RPM_BUILD_ROOT}%{libdir}
popd


# javadoc
%{__cp} -a output/dist/webapps/docs/api/* ${RPM_BUILD_ROOT}%{_javadocdir}/%{pkg_name}

# create jsp and servlet API symlinks
pushd ${RPM_BUILD_ROOT}%{_javadir}
   %{__mv} %{pkg_name}/jsp-api.jar %{pkg_name}-jsp-%{jspspec}-api.jar
   %{__ln_s} %{pkg_name}-jsp-%{jspspec}-api.jar %{pkg_name}-jsp-api.jar
   %{__mv} %{pkg_name}/servlet-api.jar %{pkg_name}-servlet-%{servletspec}-api.jar
   %{__ln_s} %{pkg_name}-servlet-%{servletspec}-api.jar %{pkg_name}-servlet-api.jar
   %{__mv} %{pkg_name}/el-api.jar %{pkg_name}-el-%{elspec}-api.jar
   %{__ln_s} %{pkg_name}-el-%{elspec}-api.jar %{pkg_name}-el-api.jar
popd

%if %{with lib}
pushd ${RPM_BUILD_ROOT}%{libdir}
    # symlink JSP and servlet API jars
    %{__ln_s} ../%{pkg_name}-jsp-%{jspspec}-api.jar .
    %{__ln_s} ../%{pkg_name}-servlet-%{servletspec}-api.jar .
    %{__ln_s} ../%{pkg_name}-el-%{elspec}-api.jar .
    %{__ln_s} $(build-classpath apache-commons-collections) commons-collections.jar
    %{__ln_s} $(build-classpath apache-commons-dbcp) commons-dbcp.jar
    %{__ln_s} $(build-classpath apache-commons-pool) commons-pool.jar
    %{__ln_s} $(build-classpath log4j) log4j.jar
    %{__ln_s} $(build-classpath ecj) jasper-jdt.jar
popd
%else
rm -Rf ${RPM_BUILD_ROOT}%{libdir}/*
pushd ${RPM_BUILD_ROOT}%{libdir}
    %{__ln_s} ../%{pkg_name}-el-%{elspec}-api.jar .
popd
%endif


# Install the maven metadata
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_mavenpomdir}
pushd output/dist/src/res/maven
for pom in *.pom; do
    # fix-up version in all pom files
    sed -i 's/@MAVEN.DEPLOY.VERSION@/%{version}/g' $pom
done

%if %{with lib}
# we won't install dbcp, juli-adapters and juli-extras pom files
for libname in annotations-api catalina jasper-el jasper catalina-ha; do
    %{__cp} -a %{pkg_name}-$libname.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{pkg_name}-$libname.pom
    %add_maven_depmap JPP.%{pkg_name}-$libname.pom %{pkg_name}/$libname.jar -f "tomcat-lib"
done
%endif

# servlet-api jsp-api and el-api are not in tomcat subdir, since they are widely re-used elsewhere
%{__cp} -a tomcat-jsp-api.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP-tomcat-jsp-api.pom
%add_maven_depmap JPP-tomcat-jsp-api.pom tomcat-jsp-api.jar -f "tomcat-jsp-api" -a "org.eclipse.jetty.orbit:javax.servlet.jsp"

%{__cp} -a tomcat-el-api.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP-tomcat-el-api.pom
%add_maven_depmap JPP-tomcat-el-api.pom tomcat-el-api.jar -f "tomcat-el-api" -a "org.eclipse.jetty.orbit:javax.el"

%{__cp} -a tomcat-servlet-api.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP-tomcat-servlet-api.pom
# Generate a depmap fragment javax.servlet:servlet-api pointing to
# tomcat-servlet-3.0-api for backwards compatibility
# also provide jetty depmap (originally in jetty package, but it's cleaner to have it here
%add_maven_depmap JPP-tomcat-servlet-api.pom tomcat-servlet-api.jar -f "tomcat-servlet-api" -a "javax.servlet:servlet-api,javax.servlet:javax.servlet-api,org.mortbay.jetty:servlet-api,org.eclipse.jetty.orbit:javax.servlet"

%if %{with lib}
# two special pom where jar files have different names
%{__cp} -a tomcat-tribes.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{pkg_name}-catalina-tribes.pom
%add_maven_depmap JPP.%{pkg_name}-catalina-tribes.pom %{pkg_name}/catalina-tribes.jar -f "tomcat-lib"

%{__cp} -a tomcat-coyote.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{pkg_name}-tomcat-coyote.pom
%add_maven_depmap JPP.%{pkg_name}-tomcat-coyote.pom %{pkg_name}/tomcat-coyote.jar -f "tomcat-lib"

%{__cp} -a tomcat-juli.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{pkg_name}-tomcat-juli.pom
%add_maven_depmap JPP.%{pkg_name}-tomcat-juli.pom %{pkg_name}/tomcat-juli.jar -f "tomcat-lib"

%{__cp} -a tomcat-api.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{pkg_name}-tomcat-api.pom
%add_maven_depmap JPP.%{pkg_name}-tomcat-api.pom %{pkg_name}/tomcat-api.jar -f "tomcat-lib"

%{__cp} -a tomcat-util.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{pkg_name}-tomcat-util.pom
%add_maven_depmap JPP.%{pkg_name}-tomcat-util.pom %{pkg_name}/tomcat-util.jar -f "tomcat-lib"
%endif

%{?scl:EOF}


%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{pkg_name}

%files jsp-%{jspspec}-api -f output/dist/src/res/maven/.mfiles-tomcat-jsp-api
%{_javadir}/%{pkg_name}-jsp-%{jspspec}*.jar
%defattr(-,root,root,-)

%if %{with lib}
%files lib -f output/dist/src/res/maven/.mfiles-tomcat-lib
%defattr(-,root,root,-)
%{libdir}
%{_mavenpomdir}/JPP.%{pkg_name}-annotations-api.pom
%{_mavenpomdir}/JPP.%{pkg_name}-catalina-ha.pom
%{_mavenpomdir}/JPP.%{pkg_name}-catalina-tribes.pom
%{_mavenpomdir}/JPP.%{pkg_name}-catalina.pom
%{_mavenpomdir}/JPP.%{pkg_name}-jasper-el.pom
%{_mavenpomdir}/JPP.%{pkg_name}-jasper.pom
%{_mavenpomdir}/JPP.%{pkg_name}-tomcat-api.pom
%{_mavenpomdir}/JPP.%{pkg_name}-tomcat-juli.pom
%{_mavenpomdir}/JPP.%{pkg_name}-tomcat-coyote.pom
%{_mavenpomdir}/JPP.%{pkg_name}-tomcat-util.pom

%exclude %{libdir}/%{pkg_name}-el-%{elspec}-api.jar
%endif

%files servlet-%{servletspec}-api -f output/dist/src/res/maven/.mfiles-tomcat-servlet-api
%defattr(-,root,root,-)
%doc LICENSE
%{_javadir}/%{pkg_name}-servlet-%{servletspec}*.jar

%files el-%{elspec}-api -f output/dist/src/res/maven/.mfiles-tomcat-el-api
%defattr(-,root,root,-)
%doc LICENSE
%{_javadir}/%{pkg_name}-el-%{elspec}-api.jar
%dir %{libdir}
%{libdir}/%{pkg_name}-el-%{elspec}-api.jar


%changelog
* Tue Jul 21 2015 Michal Srb <msrb@redhat.com> - 0:7.0.42-1.21
- Drop tomcat-lib subpackage
- Resolves: rhbz#1201916

* Thu Apr  2 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:7.0.42-1.20
- Fix duplicate file ownership

* Thu Jan 15 2015 Michael Simacek <msimacek@redhat.com> - 0:7.0.42-1.19
- Fix common directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 0:7.0.42-1.18
- Mass rebuild 2015-01-13

* Fri Jan 09 2015 Michal Srb <msrb@redhat.com> - 7.0.42-1.17
- Do not provide EE apis for JSP and EL

* Fri Jan 09 2015 Michal Srb <msrb@redhat.com> - 0:7.0.42-1.16
- Mass rebuild 2015-01-09

* Wed Jan 07 2015 Michal Srb <msrb@redhat.com> - 7.0.42-1.15
- Workaround issue with alternatives(?) on RHEL6

* Wed Jan 07 2015 Michal Srb <msrb@redhat.com> - 7.0.42-1.14
- Migrate to .mfiles

* Tue Dec 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:7.0.42-1.13
- Migrate requires and build-requires to rh-java-common

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:7.0.42-1.12
- Mass rebuild 2014-12-15

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:7.0.42-1.11
- Rebuild for rh-java-common collection

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:7.0.42-1.10
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:7.0.42-1.9
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:7.0.42-1.8
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:7.0.42-1.7
- Remove requires on java

* Tue Feb 18 2014 Michal Srb <msrb@redhat.com> - 0:7.0.42-1.6
- Fix problem with dangling symlink
- Remove unused macro definitions

* Fri Feb 14 2014 Michal Srb <msrb@redhat.com> - 0:7.0.42-1.5
- Fix BR/R

* Fri Feb 14 2014 Michal Srb <msrb@redhat.com> - 0:7.0.42-1.4
- SCL-ize inter-module deps

* Thu Feb 13 2014 Michal Srb <msrb@redhat.com> - 0:7.0.42-1.3
- Remove uneeded stuff (systemd files, sample webapps, ...)

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:7.0.42-1.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:7.0.42-1.1
- First maven30 software collection build

* Tue Jan 21 2014 David Knox <dknox@redhat.com> - 0:7.0.42-1
- Resolves: rhbz#1051657 update to 7.0.42. Ant-nodeps is
- deprecated.

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 07.0.40-3
- Mass rebuild 2013-12-27

* Sat May 11 2013 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.40-1
- Updated to 7.0.40
- Resolves: rhbz 956569 added missing commons-pool link

* Mon Mar  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:7.0.37-2
- Add depmaps for org.eclipse.jetty.orbit
- Resolves: rhbz#917626

* Wed Feb 20 2013 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.39-1
- Updated to 7.0.39

* Wed Feb 20 2013 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.37-1
- Updated to 7.0.37

* Mon Feb 4 2013 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.35-1
- Updated to 7.0.35
- systemd SuccessExitStatus=143 for proper stop exit code processing

* Mon Dec 24 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.34-1
- Updated to 7.0.34
- ecj >= 4.2.1 now required
- Resolves: rhbz 889395 concat classpath correctly; chdir to $CATALINA_HOME

* Fri Dec 7 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.33-2
- Resolves: rhbz 883806 refix logdir ownership 

* Sun Dec 2 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.33-1
- Updated to 7.0.33
- Resolves: rhbz 873620 need chkconfig for update-alternatives

* Wed Oct 17 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.32-1
- Updated to 7.0.32
- Resolves: rhbz 842620 symlinks to taglibs

* Fri Aug 24 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.29-1
- Updated to 7.0.29
- Add pidfile as tmpfile
- Use systemd for running as unprivileged user
- Resolves: rhbz 847751 upgrade path was broken
- Resolves: rhbz 850343 use new systemd-rpm macros

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:7.0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 2 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.28-1
- Updated to 7.0.28
- Resolves: rhbz 820119 Remove bundled apache-commons-dbcp
- Resolves: rhbz 814900 Added tomcat-coyote POM
- Resolves: rhbz 810775 Remove systemv stuff from %post scriptlet
- Remove redhat-lsb R 

* Mon Apr 9 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.27-2
- Fixed native download hack

* Sat Apr 7 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.27-1
- Updated to 7.0.27
- Fixed jakarta-taglibs-standard BR and R

* Wed Mar 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:7.0.26-2
- Add more depmaps to J2EE apis to help jetty/glassfish updates

* Wed Mar 14 2012 Juan Hernandez <juan.hernandez@redhat.com> 0:7.0.26-2
- Added the POM files for tomcat-api and tomcat-util (#803495)

* Wed Feb 22 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.26-1
- Updated to 7.0.26
- Bug 790334: Change ownership of logdir for logrotate

* Thu Feb 16 2012 Krzysztof Daniel <kdaniel@redhat.com> 0:7.0.25-4
- Bug 790694: Priorities of jsp, servlet and el packages updated.

* Wed Feb 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 0:7.0.25-3
- Dropped indirect dependecy to tomcat 5

* Sun Jan 22 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.25-2
- Added hack for maven depmap of tomcat-juli absolute link [ -f ] pass correctly

* Sat Jan 21 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.25-1
- Updated to 7.0.25
- Removed EntityResolver patch (changes already in upstream sources)
- Place poms and depmaps in the same package as jars
- Added javax.servlet.descriptor to export-package of servlet-api
- Move several chkconfig actions and reqs to systemv subpackage
- New maven depmaps generation method
- Add patch to support java7. (patch sent upstream).
- Require java >= 1:1.6.0

* Fri Jan 13 2012 Krzysztof Daniel <kdaniel@redhat.com> 0:7.0.23-5
- Exported javax.servlet.* packages in version 3.0 as 2.6 to make
  servlet-api compatible with Eclipse.

* Thu Jan 12 2012 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.23-4
- Move jsvc support to subpackage

* Wed Jan 11 2012 Alexander Kurtakov <akurtako@redhat.com> 0:7.0.23-2
- Add EntityResolver setter patch to jasper for jetty's need. (patch sent upstream).

* Mon Dec 12 2011 Joseph D. Wagner <joe@josephdwagner.info> 0:7.0.23-3
- Added support to /usr/sbin/tomcat-sysd and /usr/sbin/tomcat for
  starting tomcat with jsvc, which allows tomcat to perform some
  privileged operations (e.g. bind to a port < 1024) and then switch
  identity to a non-privileged user. Must add USE_JSVC="true" to
  /etc/tomcat/tomcat.conf or /etc/sysconfig/tomcat.

* Mon Nov 28 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.23-1
- Updated to 7.0.23

* Fri Nov 11 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.22-2
- Move tomcat-juli.jar to lib package
- Drop %%update_maven_depmap as in tomcat6
- Provide native systemd unit file ported from tomcat6

* Thu Oct 6 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.22-1
- Updated to 7.0.22

* Mon Oct 03 2011 Rex Dieter <rdieter@fedoraproject.org> - 0:7.0.21-3.1
- rebuild (java), rel-eng#4932

* Mon Sep 26 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.21-3
- Fix basedir mode

* Tue Sep 20 2011 Roland Grunberg <rgrunber@redhat.com> 0:7.0.21-2
- Add manifests for el-api, jasper-el, jasper, tomcat, and tomcat-juli.

* Thu Sep 8 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.21-1
- Updated to 7.0.21

* Mon Aug 15 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.20-3
- Require java = 1:1.6.0

* Mon Aug 15 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.20-2
- Require java < 1.7.0

* Mon Aug 15 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.20-1
- Updated to 7.0.20

* Tue Jul 26 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.19-1
- Updated to 7.0.19

* Tue Jun 21 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.16-1
- Updated to 7.0.16

* Mon Jun 6 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.14-3
- Added initial systemd service
- Fix some paths

* Sat May 21 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.14-2
- Fixed http source link
- Securify some permissions
- Added licenses for el-api and servlet-api
- Added dependency on jpackage-utils for the javadoc subpackage

* Sat May 14 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.14-1
- Updated to 7.0.14

* Thu May 5 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.12-4
- Provided local paths for libs
- Fixed dependencies
- Fixed update temp/work cleanup

* Mon May 2 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.12-3
- Fixed package groups
- Fixed some permissions
- Fixed some links
- Removed old tomcat6 crap

* Thu Apr 28 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.12-2
- Package now named just tomcat instead of tomcat7
- Removed Provides:  %{name}-log4j
- Switched to apache-commons-* names instead of jakarta-commons-* .
- Remove the old changelog
- BR/R java >= 1:1.6.0 , same for java-devel
- Removed old tomcat6 crap

* Wed Apr 27 2011 Ivan Afonichev <ivan.afonichev@gmail.com> 0:7.0.12-1
- Tomcat7
