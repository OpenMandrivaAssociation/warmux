#SPEC by Julien Catalano

Summary:	Free (Libre) clone of Worms from Team17 but no Wormux fork
Name:		warmux
Version:	11.04.1
Release:	4
License:	GPLv2+
Group:		Games/Arcade
Url:		http://www.warmux.org/
Source0:	http://download.gna.org/warmux/%{name}-%{version}.tar.bz2
Patch0:		warmux-zlib.patch
Patch1:		warmux-gcc47.patch
BuildRequires:	imagemagick
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml++-2.6)
BuildRequires:	pkgconfig(libpng)

%description
Almost everyone has heard of the Worms(R) series of games, developed by Team17.
Worms was created in 1990, the goal of the game consisting of a several teams
of "worms" fighting to the death on a 2D map. Warmux is heavily influenced by
all games in this genre, including Scorched Earth and Liero.

Warmux is free software clone of this game concept. Though currently under
heavy development, it is already very playable, with lots of weapons
(Dynamite, Baseball Bat, Teleportation, etc.). There are also lots of maps
available for your battling pleasure! Warmux takes the genre to the next
level, with great customisation options leading to great gameplay. There
is a wide selection of teams, from the Aliens to the Chickens. Also, new
battlefields can be downloaded from the Internet, making strategy an
important part of each battle.

Though two human players are currently needed to play (unless you have
a split personality :) the creation of artificial players and network play
are future goals. So, start downloading today, and fight to become king of
the garden!

%prep
#temp fix, 11.04.1 contains only warmux-11.04 and no warmux-11.04.1
%setup -q -n %{name}-11.04
%patch0 -p1
%patch1 -p1

%build
#(tpg) get rid of -Werror
# sed -i -e 's/-Werror//' src/Makefile.am

%configure2_5x	\
	--bindir=%{_gamesbindir} \
	--with-datadir-name=%{_gamesdatadir}/%{name} \
	--disable-rpath \
	--enable-fribidi

#(tpg) get rid of -Werror
# sed -i -e 's/-Werror//' src/Makefile.in

%make

%install
# allow this script to be executed
chmod +x install-sh

# drop icon extension
perl -pi -e 's/.png//g' data/warmux.desktop

%makeinstall_std localedir=%{_datadir}/locale

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_gamesbindir}/%{name}
%{_gamesbindir}/%{name}-list-games
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}_files.desktop
%{_datadir}/pixmaps/%{name}_128x128.png
%{_mandir}/man6/%{name}.*

