%global tl_name tikz-feynhand
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.0
Release:	%{tl_revision}.1
Summary:	Feynman diagrams with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-feynhand
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-feynhand.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-feynhand.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package lets you draw Feynman diagrams using TikZ. It is a low-end
modification of the TikZ-Feynman package, one of whose principal
advantages is the automatic generation of diagrams, for which it needs
LuaTeX. TikZ-FeynHand only provides the manual mode and hence runs in
LaTeX without any reference to LuaTeX. In addition it provides some new
styles for vertices and propagators, alternative shorter keywords in
addition to TikZ-Feynman's longer ones, some shortcut commands for
quickly customizing the diagrams' look, and the new feature of putting
one propagator "on top" of another. It also includes a quick user guide
for getting started, with many examples and a 5-minute introduction to
TikZ.

