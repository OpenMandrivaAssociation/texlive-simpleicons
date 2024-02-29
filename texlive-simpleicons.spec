Name:		texlive-simpleicons
Version:	70117
Release:	1
Summary:	Simple Icons for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/simpleicons
License:	cc-by-1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simpleicons.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simpleicons.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Similar to FontAwesome icons being provided on LaTeX by the
fontawesome package, this package aims to do the same with
Simple Icons. For reference, visit their website:
https://simpleicons.org/.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/simpleicons
%{_texmfdistdir}/fonts/type1/public/simpleicons
%{_texmfdistdir}/fonts/tfm/public/simpleicons
%{_texmfdistdir}/fonts/opentype/public/simpleicons
%{_texmfdistdir}/fonts/map/dvips/simpleicons
%{_texmfdistdir}/fonts/enc/dvips/simpleicons
%doc %{_texmfdistdir}/doc/fonts/simpleicons

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
