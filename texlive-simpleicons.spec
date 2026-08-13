%global tl_name simpleicons
%global tl_revision 79907
%global tl_version 16.28.0

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Simple Icons for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/simpleicons
License:	cc0
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simpleicons.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simpleicons.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Similar to FontAwesome icons being provided on LaTeX by the fontawesome
package, this package aims to do the same with Simple Icons. For
reference, visit their website: https://simpleicons.org/.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from simpleicons:
Map simpleicons.map
TL_DROPIN_EOF
