Summary:	CmdTool2 SAS RAID Management Utility
Name:		CmdTool2
Version:	5.00.08
Release:	1
License:	LSI
Group:		Base
Source0:	http://downloadmirror.intel.com/17867/eng/CMDTool2_Linux_v%{version}.zip
# Source0-md5:	f3243e091de00e393e0687d29a7199d2
URL:		http://downloadcenter.intel.com/detail_desc.aspx?DwnldID=17867
BuildRequires:	rpm-utils
BuildRequires:	unzip
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin
%define		_enable_debug_packages	0

%description
CmdTool2 is used to manage Intel(R) SAS RAID controllers. It can be used to
query the controller and attached devices for status, Update Firmware, and
create/manage logical drive configuration.

Tool is valid for following controllers:
- Intel RAID Controller RS2BL040
- Intel RAID Controller RS2BL080
- Intel RAID Controller RS2PI008
- Intel RAID Controller SRCSAS144E
- Intel RAID Controller SRCSAS18E
- Intel RAID Controller SRCSASBB8I
- Intel RAID Controller SRCSASJV
- Intel RAID Controller SRCSASLS4I
- Intel RAID Controller SRCSASPH16I
- Intel RAID Controller SRCSASRB
- Intel RAID Controller SRCSATAWB

See the readme flie for greater detail on installation and usage.

%prep
%setup -q -c
rpm2cpio *.rpm | cpio -i -d

mv opt/MegaRAID/CmdTool2/CmdTool2 .
mv CMDTool2_Linux_v%{version}_rel-notes.txt rel-notes.txt
mv "Web License.rtf" Web_License.rtf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -p CmdTool2 $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rel-notes.txt Web_License.rtf
%attr(755,root,root) %{_sbindir}/CmdTool2
