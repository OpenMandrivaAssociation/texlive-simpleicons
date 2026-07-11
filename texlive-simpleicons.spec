%global tl_name simpleicons
%global tl_revision 79577

Name:		texlive-%{tl_name}
Epoch:		1
Version:	16.24.1
Release:	%{tl_revision}.1
Summary:	Simple Icons for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/simpleicons
License:	cc0
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simpleicons.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simpleicons.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Similar to FontAwesome icons being provided on LaTeX by the fontawesome
package, this package aims to do the same with Simple Icons. For
reference, visit their website: https://simpleicons.org/.

