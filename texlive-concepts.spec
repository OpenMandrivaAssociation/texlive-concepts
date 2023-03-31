Name:		texlive-concepts
Version:	29020
Release:	2
Summary:	Keeping track of formal 'concepts' for a particular field
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/concepts
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concepts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concepts.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package helps to keep track of formal 'concepts' for a
specific field or document. This is particularly useful for
scientific papers (for example, in physics, mathematics or
computer science), which may introduce several concepts (with
their own symbols). The package's commands allow the user to
define a concept (typically, near its first use), and will
ensure consistent use throughout the document. The package
depends on several other packages; while these are fairly
common packages, the user should check the package's README
file for the complete list.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/concepts/concepts.sty
%doc %{_texmfdistdir}/doc/latex/concepts/README
%doc %{_texmfdistdir}/doc/latex/concepts/concepts.pdf
%doc %{_texmfdistdir}/doc/latex/concepts/concepts.tex
%doc %{_texmfdistdir}/doc/latex/concepts/dry.sty
%doc %{_texmfdistdir}/doc/latex/concepts/packagedoc.cls
%doc %{_texmfdistdir}/doc/latex/concepts/with.sty

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
