%global tl_name concepts
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0.5~r1
Release:	%{tl_revision}.1
Summary:	Keeping track of formal concepts for a particular field
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/concepts
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/concepts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/concepts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package helps to keep track of formal 'concepts' for a specific
field or document. This is particularly useful for scientific papers
(for example, in physics, mathematics or computer science), which may
introduce several concepts (with their own symbols). The package's
commands allow the user to define a concept (typically, near its first
use), and will ensure consistent use throughout the document. The
package depends on several other packages; while these are fairly common
packages, the user should check the package's README file for the
complete list.

