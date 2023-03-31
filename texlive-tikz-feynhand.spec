Name:		texlive-tikz-feynhand
Version:	51915
Release:	2
Summary:	Feynman diagrams with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-feynhand
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-feynhand.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-feynhand.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package lets you draw Feynman diagrams using TikZ. It is a
low-end modification of the TikZ-Feynman package, one of whose
principal advantages is the automatic generation of diagrams,
for which it needs LuaTex. TikZ-FeynHand only provides the
manual mode and hence runs in LaTeX without any reference to
LuaTeX. In addition it provides some new styles for vertices
and propagators, alternative shorter keywords in addition to
TikZ-Feynman's longer ones, some shortcut commands for quickly
customizing the diagrams' look, and the new feature of putting
one propagator "on top" of another. It also includes a quick
user guide for getting started, with many examples and a
5-minute introduction to TikZ.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-feynhand
%doc %{_texmfdistdir}/doc/latex/tikz-feynhand

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
