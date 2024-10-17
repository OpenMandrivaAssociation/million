Name:		million
Version:	1.0.2
Release:	1
Summary:	Who Wants To Be A Millionaire game (Russian version)
Group:		Games/Puzzles
License:	Freeware
URL:		https://dansoft.krasnokamensk.ru/more.html?id=1012
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(xrender) >= 0.9.6
Requires:	qt5-database-plugin-sqlite

%description
Who Wants To Be A Millionaire? is a game after quiz TV show.
This is Russian version of the game. No other languages are supported.

%prep
%setup -q

%build
%qmake_qt5 %{name}.pro
%make

%install
%__rm -rf %{buildroot}

# install binary
%__mkdir_p %{buildroot}%{_bindir}
%__cp Bin/%{name} %{buildroot}%{_bindir}/

# install game data
mkdir -p %{buildroot}%{_datadir}/%{name}
cp Bin/%{name}.db %{buildroot}%{_datadir}/%{name}/
cp -r Bin/sounds %{buildroot}%{_datadir}/%{name}/

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
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

