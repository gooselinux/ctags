Summary: A C programming language indexing and/or cross-reference tool
Name: ctags
Version: 5.8
Release: 2%{?dist}
License: GPLv2+ or Public Domain
Group: Development/Tools
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0: ctags-5.7-destdir.patch
Patch1: ctags-5.7-segment-fault.patch
URL: http://ctags.sourceforge.net/
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Ctags generates an index (or tag) file of C language objects found in
C source and header files.  The index makes it easy for text editors or
other utilities to locate the indexed items.  Ctags can also generate a
cross reference file which lists information about the various objects
found in a set of C language files in human readable form.  Exuberant
Ctags improves on ctags because it can find all types of C language tags,
including macro definitions, enumerated values (values inside enum{...}),
function and method definitions, enum/struct/union tags, external
function prototypes, typedef names and variable declarations.  Exuberant
Ctags is far less likely to be fooled by code containing #if preprocessor
conditional constructs than ctags.  Exuberant ctags supports output of
Emacs style TAGS files and can be used to print out a list of selected
objects found in source files.

Install ctags if you are going to use your system for C programming.

%package etags
Summary: Exuberant Ctags for emacs tag format
Group: Development/Tools
Requires: ctags = %{version}-%{release}
Requires: /usr/sbin/alternatives

%description etags
This package will generate tags in a format which GNU Emacs understand,
it's a alternativ implementation of the GNU etags program.
Note: some command line options is not compatible with GNU etags.


%prep
%setup -q
%patch0 -p1 -b .destdir
%patch1 -p1 -b .crash

%build
%configure

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make DESTDIR=%{buildroot} install

pushd %{buildroot}%{_bindir}
ln -s ctags etags.ctags
popd

pushd %{buildroot}%{_mandir}/man1
ln -s ctags.1.gz etags.ctags.1.gz
popd

%posttrans etags
/usr/sbin/alternatives --install /usr/bin/etags emacs.etags /usr/bin/etags.ctags 20 \
   --slave /usr/share/man/man1/etags.1.gz emacs.etags.man /usr/share/man/man1/ctags.1.gz

%postun etags
/usr/sbin/alternatives --remove etags /usr/bin/etags.ctags || :

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc COPYING EXTENDING.html FAQ NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files etags
%defattr(-, root, root, -)
%doc COPYING
%{_bindir}/etags.%{name}
%{_mandir}/man1/etags.%{name}.1*

%changelog
* Mon Jan  4 2010 Marcela Mašláňová <mmaslano@redhat.com> - 5.8-2
- fix license tag for review
- Resolves: rhbz#552228

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 5.8-1.1
- Rebuilt for RHEL 6

* Tue Sep 01 2009 Than Ngo <than@redhat.com> - 5.8-1
- 5.8
- apply patch to fix segment fault, thanks to Masatake YAMATO

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 29 2008 Than Ngo <than@redhat.com>  5.7-3
- add subpackage ctags-etags

* Tue Jul 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> 5.7-2
- fix license tag

* Fri Feb 15 2008 Than Ngo <than@redhat.com> 5.7-1
- 5.7
- merge review: ctags

* Mon Jul 17 2006 Nalin Dahyabhai <nalin@redhat.com> 5.6-1.1
- rebuild

* Tue Jun 06 2006 Than Ngo <than@redhat.com> 5.6-1
- update to 5.6

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 5.5.4-4.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 5.5.4-4.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sun Jul 31 2005 Florian La Roche <laroche@redhat.com>
- remove etags

* Thu Mar 03 2005 Than Ngo <than@redhat.com> 5.5.4-3
- rebuilt

* Wed Feb 09 2005 Than Ngo <than@redhat.com> 5.5.4-2
- rebuilt

* Thu Jun 17 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- 5.5.4

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Sep 27 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- 5.5.2, no patch needed anymore

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May  6 2003 Than Ngo <than@redhat.com> 5.5-1
- 5.5

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Nov 13 2002 Karsten Hopp <karsten@redhat.de>
- update to 5.4

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 18 2002 Than Ngo <than@redhat.com> 5.2.3-3
- don't forcibly strip binaries

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed May 22 2002 Harald Hoyer <harald@redhat.de>
- 5.2.3

* Tue Feb 26 2002 Than Ngo <than@redhat.com> 5.2.2-2
- rebuild in new enviroment

* Tue Feb 19 2002 Bernhard Rosenkraenzer <bero@redhat.com> 5.2.2-1
- 5.2.2

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jul 11 2001 Jakub Jelinek <jakub@redhat.com>
- rebuilt against binutils-2.11.90.0.8-3 to reserve .dynamic space

* Mon Jun 11 2001 Preston Brown <pbrown@redhat.com>
- 5.0.1

* Thu Jan 04 2001 Preston Brown <pbrown@redhat.com>
- 4.0.3
- remove etags, it is not fully compatible with cmd line of GNU etags.

* Sun Jul 16 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 4.0.2 from sourceforge

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sat Jun 17 2000 Matt Wilson <msw@redhat.com>
- added defattr

* Mon Jun 12 2000 Preston Brown <pbrown@redhat.com>
- FHS paths

* Mon May  8 2000 Bernhard Rosenkränzer <bero@redhat.com>
- Update to 3.5.2
- minor cleanups to spec file

* Tue Feb 16 2000 Bernhard Rosenkränzer <bero@redhat.com>
- Update to 3.4 to fix bug #9446

* Thu Feb 03 2000 Preston Brown <pbrown@redhat.com>
- compress man page.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)
- version 3.2

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 2.0.3

* Mon Nov 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- removed etags.  Emacs provides its own; and needs to support
  more than just C.

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from 1.5 to 1.6

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
