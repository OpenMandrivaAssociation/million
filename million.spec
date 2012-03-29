Name:		million
Version:	1.0.0
Release:	%mkrel 1
Summary:	Who Wants To Be A Millionaire game (Russian version)
Group:		Games/Puzzles
License:	Freeware
URL:		http://dansoft.krasnokamensk.ru/more.html?id=1012
Source0:	%{name}-%{version}.tar.bz2
Source1:	million-license.txt
Patch0:		million-1.0.0-datapath.patch
BuildRequires:	qt4-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(xrender) >= 0.9.6

%description
Who Wants To Be A Millionaire? is a game after quiz TV show.
This is Russian version of the game. No other languages are supported.

%prep
%setup -q
%patch0 -p1
%__cp %{SOURCE1} COPYING

%build
%qmake_qt4 %{name}.pro
%make

%install
%__rm -rf %{buildroot}

# install binary
%__mkdir_p %{buildroot}%{_bindir}
%__cp Bin/%{name} %{buildroot}%{_bindir}/

# install game data
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp Bin/%{name}.db %{buildroot}%{_datadir}/%{name}/
%__cp -r Bin/sounds %{buildroot}%{_datadir}/%{name}/

# create and install icons
for N in 16 32 48 64 128; do convert images/logo.png -scale ${N}x${N}! $N.png; done
%__install -D 16.png -m 644 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%__install -D 32.png -m 644 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%__install -D 48.png -m 644 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%__install -D 64.png -m 644 %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%__install -D 128.png -m 644 %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

# XDG menu entry
%__mkdir_p  %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=Who Wants To Be A Millionaire?
Name[ru]=Кто хочет стать миллионером?
Comment=Quiz game after TV show
Comment[ru]=Аналог знаменитой телеигры
Icon=%{name}
Exec=%{name}
Terminal=false
Categories=Game;LogicGame;
EOF

%clean
%__rm -rf %{buildroot}

%files
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

