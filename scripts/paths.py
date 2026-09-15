"""Where an episode's files live, in one place.

Every build script used to carry its own copy of two constants: the repo
directory under episodes/ and the media directory on E:. Both spelled
s01-venezia-pali, so a second episode could not run without editing seven
files, and running one of them from muscle memory would have written s02's
output over s01's.

    from paths import Episode
    ep = Episode("s01-venezia-pali")
    ep.script            episodes/s01-venezia-pali/script.md
    ep.clips / "G1.mp4"  E:/.../archi-shorts/s01-venezia-pali/clips/G1.mp4

The media root is overridable with ARCHI_SHORTS_MEDIA so the tests can point
at a fixture tree, and so a machine without the E: drive is not simply stuck.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"


def episodes_root() -> Path:
    """Overridable so the golden tests can run against a copy of an episode
    rather than writing over the committed one."""
    return Path(os.environ.get("ARCHI_SHORTS_EPISODES", REPO / "episodes"))

# Starter-kit default: media lives under the kit root's media/ folder.
# Override with ARCHI_SHORTS_MEDIA if the media should live elsewhere.
DEFAULT_MEDIA_ROOT = Path.cwd() / "media"
REFERENCE_ROOT = Path.cwd() / "media" / "reference"


def media_root() -> Path:
    return Path(os.environ.get("ARCHI_SHORTS_MEDIA", DEFAULT_MEDIA_ROOT))


@dataclass(frozen=True)
class Episode:
    """An episode id (the directory name) and the paths that follow from it."""

    name: str

    def __post_init__(self) -> None:
        if not self.name or "/" in self.name or "\\" in self.name:
            raise SystemExit(f"not an episode id: {self.name!r}")

    @property
    def slug(self) -> str:
        """The short id media filenames are built from: s01-venezia-pali -> s01."""
        return self.name.split("-", 1)[0]

    # --- repo side -------------------------------------------------------
    @property
    def repo(self) -> Path:
        return episodes_root() / self.name

    @property
    def script(self) -> Path:
        return self.repo / "script.md"

    @property
    def edl(self) -> Path:
        return self.repo / "edl.json"

    @property
    def boundaries(self) -> Path:
        return self.repo / "cut_boundaries.json"

    @property
    def captions(self) -> Path:
        return self.repo / "captions.json"

    @property
    def overlays(self) -> Path:
        return self.repo / "overlays.json"

    # --- media side ------------------------------------------------------
    @property
    def media(self) -> Path:
        return media_root() / self.name

    @property
    def clips(self) -> Path:
        return self.media / "clips"

    @property
    def audio(self) -> Path:
        return self.media / "audio"

    @property
    def renders(self) -> Path:
        return self.media / "renders"

    # --- checks ----------------------------------------------------------
    def require_repo(self) -> Path:
        """The episode directory must exist; a typo should not create one."""
        if not self.repo.is_dir():
            known = sorted(p.name for p in episodes_root().iterdir() if p.is_dir())
            raise SystemExit(f"no episode {self.name!r} in episodes/. known: {', '.join(known)}")
        return self.repo

    def require_media(self) -> Path:
        if not self.media.is_dir():
            raise SystemExit(
                f"no media directory for {self.name} at {self.media}\n"
                "set ARCHI_SHORTS_MEDIA if the working drive is mounted elsewhere")
        return self.media


def add_episode_argument(ap) -> None:
    """The one flag every build script takes.

    Deliberately required. A default of s01-venezia-pali is how a script run
    for s02 quietly rebuilds s01 instead.
    """
    ap.add_argument("--episode", required=True, metavar="ID",
                    help="episode directory name, e.g. s01-venezia-pali")


def episode_from_args(args) -> Episode:
    ep = Episode(args.episode)
    ep.require_repo()
    return ep
