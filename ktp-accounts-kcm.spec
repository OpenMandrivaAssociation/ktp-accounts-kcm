Summary:	KAccouts integration for KDE Telepathy contacts
Name:		ktp-accounts-kcm
Version:	22.12.2
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Designer)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5ScriptTools)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5WebKit)
BuildRequires:	cmake(Qt5TextToSpeech)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Runner)
BuildRequires:	cmake(KAccounts)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(TelepathyQt5)
BuildRequires:	cmake(KTp)
BuildRequires:	intltool
BuildRequires:	pkgconfig(libaccounts-glib)
Requires:	telepathy-haze
Requires:	telepathy-gabble
Requires:	telepathy-salut
Requires:	telepathy-idle

%description
KAccounts integration for KDE Telepathy contacts.

%files -f all.lang
%{_libdir}/libktpaccountskcminternal.so.*
%{_libdir}/qt5/plugins/kaccounts/ui/ktpaccountskcm_plugin_kaccounts.so
%{_libdir}/qt5/plugins/ktpaccountskcm_plugin_gabble.so
%{_libdir}/qt5/plugins/ktpaccountskcm_plugin_haze.so
%{_libdir}/qt5/plugins/ktpaccountskcm_plugin_idle.so
%{_libdir}/qt5/plugins/ktpaccountskcm_plugin_morse.so
%{_libdir}/qt5/plugins/ktpaccountskcm_plugin_sipe.so
%{_libdir}/qt5/plugins/ktpaccountskcm_plugin_sunshine.so
%{_libdir}/qt5/plugins/ktpaccountskcm_plugin_salut.so
%{_datadir}/accounts/providers/kde/*.provider
%{_datadir}/accounts/services/kde/*.service
%{_datadir}/kservices5/ktpaccountskcm*.desktop
%{_datadir}/kservicetypes5/ktpaccountskcminternal-accountuiplugin.desktop
%{_datadir}/telepathy/profiles/*

%prep
%setup -q
%autopatch -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kcm_ktp_accounts
%find_lang kcmtelepathyaccounts_plugin_butterfly
%find_lang kcmtelepathyaccounts_plugin_gabble
%find_lang kcmtelepathyaccounts_plugin_haze
%find_lang kcmtelepathyaccounts_plugin_idle
%find_lang kcmtelepathyaccounts_plugin_morse
%find_lang kcmtelepathyaccounts_plugin_pintxo
%find_lang kcmtelepathyaccounts_plugin_rakia
%find_lang kcmtelepathyaccounts_plugin_salut
%find_lang kcmtelepathyaccounts_plugin_sipe
%find_lang kcmtelepathyaccounts_plugin_sunshine

cat *.lang >all.lang
