\LoadClass[a4paper,11pt]{article}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{physics_article}[18/05/15 - Article class for reports written by Nottingham Physics students, without biblatex]

\RequirePackage{fancyhdr}
% this package is used to provide and populate the header and footer
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{graphicx}
%package used to include figures as encapsulated postscript
\RequirePackage{hyperref}


\renewcommand{\familydefault}{cmss}

\setlength{\hoffset}{-0.4mm}
\setlength{\voffset}{-0.4mm}
\setlength{\oddsidemargin}{5mm}
\setlength{\topmargin}{5mm}
\setlength{\headheight}{5mm}
\setlength{\headsep}{5mm}
\setlength{\textheight}{227mm}
\setlength{\textwidth}{150mm}
\setlength{\marginparsep}{10mm}
\setlength{\footskip}{10mm}

\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.4pt}

\pagestyle{fancy}

\def\studentid#1{\gdef\@studentid{#1}}
\def\myname#1{\gdef\@myname{#1}}
\def\mytitle#1{\gdef\@mytitle{#1}}

\lhead{Student id: \@studentid}
\chead{}
\rhead{\@myname}
\lfoot{}
\cfoot{\thepage}
\rfoot{}

\author{\@myname \\School of Physics and Astronomy\\University of Nottingham}
\title{\@mytitle}