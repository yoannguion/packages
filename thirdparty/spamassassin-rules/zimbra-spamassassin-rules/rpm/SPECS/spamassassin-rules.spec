Summary:            Default ruleset for SpamAssassin
Name:               zimbra-spamassassin-rules
Version:            1.0.0
Release:            1zimbra8.8b5ZAPPEND
License:            Apache-2.0
Requires:           zimbra-mta-base, zimbra-perl-mail-spamassassin >= 3.4.6-1zimbra8.8b3ZAPPEND
Packager:           Zimbra Packaging Services <packaging-devel@zimbra.com>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%description
Default ruleset for SpamAssassin

%changelog
* Mon Mar 28 2022 Zimbra Packaging Services <packaging-devel@zimbra.com> - VERSION-1zimbra8.8b5ZAPPEND
- Fix ZCS-11117, Upgraded spamassassin to 3.4.6
* Wed Apr 08 2021 Zimbra Packaging Services <packaging-devel@zimbra.com> - VERSION-1zimbra8.8b4ZAPPEND
-Upgraded spamAssasin to 3.4.5
* Sat Dec 05 2020 Zimbra Packaging Services <packaging-devel@zimbra.com> - VERSION-1zimbra8.8b3ZAPPEND
- Updated spamassassin with zimbra-perl-mail-dkim
* Thu Sep 10 2020 Zimbra Packaging Services <packaging-devel@zimbra.com> - VERSION-1zimbra8.8b2ZAPPEND
- Updated spamAssasin with perl-mail-dkim
* Wed Apr 1 2020 Zimbra Packaging Services <packaging-devel@zimbra.com> - VERSION-1zimbra8.8b1ZAPPEND
-Upgraded spamAssasin to 3.4.4

%install
mkdir -p ${RPM_BUILD_ROOT}/opt/zimbra/data/spamassassin/rules
cp ../../../rules/updates_spamassassin_org/* ${RPM_BUILD_ROOT}/opt/zimbra/data/spamassassin/rules/
rm -rf ${RPM_BUILD_ROOT}/opt/zimbra/data/spamassassin/rules/user_prefs.template
rm -rf ${RPM_BUILD_ROOT}/opt/zimbra/data/spamassassin/rules/languages

%files
%defattr(-,zimbra,zimbra)
/opt/zimbra/data/spamassassin/rules
