%define src_repo_tag   R0_5_0
%define eclipse_base   %{_libdir}/eclipse
%define install_loc    %{_libdir}/eclipse/dropins/valgrind
%define qualifier      201003171651

# Package in %%{_libdir} but no native code so no debuginfo
%global debug_package %{nil}

Name:           eclipse-valgrind
Version:        0.5.0
Release:        1%{?dist}
Summary:        Valgrind Tools Integration for Eclipse

Group:          Development/Tools
License:        EPL
URL:            http://www.eclipse.org/linuxtools/projectPages/valgrind
Source0:        %{name}-fetched-src-%{src_repo_tag}.tar.bz2
Source1:        %{name}-fetch-src.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#No CDT on ppc64
ExclusiveArch: %{ix86} x86_64

BuildRequires: java-devel >= 1.5.0
BuildRequires: eclipse-cdt >= 1:6.0.0
BuildRequires: eclipse-linuxprofilingframework >= 0.3.0
BuildRequires: eclipse-birt >= 2.5
BuildRequires: eclipse-pde >= 1:3.5.0
Requires: eclipse-platform >= 1:3.5.0
Requires: eclipse-cdt >= 1:6.0.0
Requires: eclipse-linuxprofilingframework >= 0.3.0
Requires: eclipse-birt >= 2.5
Requires: valgrind >= 3.3.0

%description
This package for Eclipse allows users to launch their C/C++ Development Tools
projects using the Valgrind tool suite and presents the results in the IDE. 

%prep
%setup -q -n %{name}-fetched-src-%{src_repo_tag}

%build
%{eclipse_base}/buildscripts/pdebuild \
    -f org.eclipse.linuxtools.valgrind \
    -d "cdt linuxprofilingframework emf rhino birt" \
    -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier}"

%install
%{__rm} -rf %{buildroot}
install -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/org.eclipse.linuxtools.valgrind.zip 

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{install_loc}
%doc org.eclipse.linuxtools.valgrind-feature/epl-v10.html

%changelog
* Mon Mar 22 2010 Alexander Kurtakov <akurtako@redhat.com> 0.5.0-1
- Rebase to 0.5.0.

* Wed Jan 13 2010 Andrew Overholt <overholt@redhat.com> 0.4.1-1
- Upstream 0.4.1 release.

* Wed Dec 16 2009 Alexander Kurtakov <akurtako@redhat.com> 0.4.0-0.2
- Make it Exclusive %{ix86} x86_64.

* Tue Nov 3 2009 Elliott Baron <ebaron@fedoraproject.org> 0.4.0-0.1
- Pre-release of 0.4.0.

* Thu Aug 20 2009 Elliott Baron <ebaron@fedoraproject.org> 0.3.0-1
- Upstream 0.3.0 release.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 2 2009 Elliott Baron <ebaron@redhat.com> 0.2.1-2
- Fix Massif parsing for unknown symbols (Eclipse#281417).

* Mon Jun 8 2009 Elliott Baron <ebaron@redhat.com> 0.2.1-1
- Upstream 0.2.1 release.

* Thu May 21 2009 Elliott Baron <ebaron@redhat.com> 0.2.0-2
- Adding cachegrind plugin to fetch script.

* Wed May 13 2009 Elliott Baron <ebaron@redhat.com> 0.2.0-1
- Upstream 0.2.0 release.

* Wed Apr 8 2009 Elliott Baron <ebaron@redhat.com> 0.1.0-6
- Don't generate debuginfo (rhbz#494719).

* Mon Mar 23 2009 Elliott Baron <ebaron@redhat.com> 0.1.0-5
- Rebuild for changes in pdebuild to not ship p2 metadata.

* Fri Mar 13 2009 Elliott Baron <ebaron@redhat.com> 0.1.0-4
- Fixed Massif parser crashing on other locales.

* Fri Mar 6 2009 Elliott Baron <ebaron@redhat.com> 0.1.0-3
- Changing to arch dependent for CDT dependency.
- Setting minimum Valgrind requirement to 3.3.0. 

* Thu Feb 26 2009 Elliott Baron <ebaron@redhat.com> 0.1.0-2
- No eclipse-cdt on ppc64 -> ExcludeArch.

* Mon Feb 17 2009 Elliott Baron <ebaron@redhat.com> 0.1.0-1
- Initial package.
