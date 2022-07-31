Summary:	Library providing a simple API to read and write INI-style configuration files
Name:		simpleini
Version:	4.19
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	https://github.com/brofield/simpleini/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d5d22ad20322fda1a47bcd4387b0fa1e
URL:		https://github.com/brofield/simpleini
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A cross-platform library that provides a simple API to read and write
INI-style configuration files. It supports data files in ASCII, MBCS
and Unicode.

Feature summary:
- MIT Licence allows free use in all software (including GPL and
  commercial)
- multi-platform (Windows 95 to Windows 10, Windows CE, Linux, Unix)
- loading and saving of INI-style configuration files
- configuration files can have any newline format on all platforms
- liberal acceptance of file format
  * key/values with no section, keys with no value
  * removal of whitespace around sections, keys and values
- support for multi-line values (values with embedded newline
  characters)
- optional support for multiple keys with the same name
- optional case-insensitive sections and keys (for ASCII characters
  only)
- saves files with sections and keys in the same order as they were
  loaded
- preserves comments on the file, section and keys where possible
- supports both char or wchar_t programming interfaces
- supports both MBCS (system locale) and UTF-8 file encodings
- system locale does not need to be UTF-8 on Linux/Unix to load UTF-8
  file
- support for non-ASCII characters in section, keys, values and
  comments
- support for non-standard character types or file encodings via
  user-written converter classes
- support for adding/modifying values programmatically
- should compile with no warnings in most compilers

%package devel
Summary:	Library providing a simple API to read and write INI-style configuration files
Group:		Development/Libraries
Requires:	libstdc++-devel

%description devel
A cross-platform library that provides a simple API to read and write
INI-style configuration files. It supports data files in ASCII, MBCS
and Unicode.

Feature summary:
- MIT Licence allows free use in all software (including GPL and
  commercial)
- multi-platform (Windows 95 to Windows 10, Windows CE, Linux, Unix)
- loading and saving of INI-style configuration files
- configuration files can have any newline format on all platforms
- liberal acceptance of file format
  * key/values with no section, keys with no value
  * removal of whitespace around sections, keys and values
- support for multi-line values (values with embedded newline
  characters)
- optional support for multiple keys with the same name
- optional case-insensitive sections and keys (for ASCII characters
  only)
- saves files with sections and keys in the same order as they were
  loaded
- preserves comments on the file, section and keys where possible
- supports both char or wchar_t programming interfaces
- supports both MBCS (system locale) and UTF-8 file encodings
- system locale does not need to be UTF-8 on Linux/Unix to load UTF-8
  file
- support for non-ASCII characters in section, keys, values and
  comments
- support for non-standard character types or file encodings via
  user-written converter classes
- support for adding/modifying values programmatically
- should compile with no warnings in most compilers

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}

cp -p SimpleIni.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENCE.txt README.md
%{_includedir}/SimpleIni.h
