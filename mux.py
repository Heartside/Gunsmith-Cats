from muxtools import GlobSearch, Premux, Setup, SubFile, TmdbConfig, mux, SubFilePGS

for i in range(1, 4):
    setup = Setup(
        f"{i:02d}",
        None,
        out_dir=R"Gunsmith Cats (1995) - S01 (BD Remux 1080p AVC FLAC) [Dual-Audio] [Heartside]",
        mkv_title_naming="",
        out_name=Rf"[Heartside] Gunsmith Cats (1995) - S01E$ep$ (BD Remux 1080p AVC FLAC) [$crc32$]",
        clean_work_dirs=True,
        error_on_danger=True
    )

    premux = GlobSearch(f"./{setup.episode}/Gunsmith Cats - {setup.episode} - Premux*.mkv")

    dialogue = SubFile(f"./{setup.episode}/Gunsmith Cats - {setup.episode} - Dialogue.ass").clean_styles().clean_garbage().clean_comments()

    dubtitles= SubFile(f"./{setup.episode}/Gunsmith Cats - {setup.episode} - Dubtitles.ass").clean_styles().clean_garbage().clean_comments()

    takeshi = SubFilePGS(f"./{setup.episode}/Gunsmith Cats - {setup.episode} - Takeshi.sup")

    kenichi = SubFilePGS(f"./{setup.episode}/Gunsmith Cats - {setup.episode} - Kenichi.sup")

    matt = SubFilePGS(f"./{setup.episode}/Gunsmith Cats - {setup.episode} - Matt.sup")
    
    fonts = dialogue.collect_fonts(use_system_fonts=False)

    premux = Premux(
        premux
    )

    mux(
        premux,
        dialogue.to_track("Full Subtitles [Heartside]", "eng", default=True, forced=False),
        dubtitles.to_track("Dubtitles (SDH) [Heartside]", "eng", default=False, forced=False),
        takeshi.to_track("Commentary by Takeshi Mori and Hiroki Sato [USBD]", default=False, forced=False),
        kenichi.to_track("Commentary by Kenichi Sonoda, Masahiro Arai, and Takanori Kaza'ana [USBD]", default=False, forced=False),
        matt.to_track("Commentary by Matt Greenfield and Tiffany Grant [USBD]", default=False, forced=False),
        *fonts,
        tmdb=TmdbConfig(22831, season=1)
    )