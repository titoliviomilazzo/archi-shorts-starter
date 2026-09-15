"""Draw the reference's title and label treatments as ASS events.

Looking at reference A at full resolution settles what style-contract 6 left at
`확인 필요`. Two different things are on that screen:

* The red annotation layer -- boxes, leader lines, dimension figures -- is
  **rendered into the video by the model**. Its Korean is misspelled
  ("김믹 징장: 3쳠 4.5 시넘") and its figures are garbled, which is what
  generated text looks like. It is not an editor overlay.
* The white title is an overlay, and it is not a caption in a bigger size:
  no black stroke, tracking near 40% of the glyph, and often a smaller second
  line under it. The reference also sets a single corner bracket at its top
  left; that is available behind `"bracket": true` but off by default -- the
  owner read the unpaired mark as a mistake rather than an ornament.

Flow cannot spell Korean, so our labels have to be overlays even though the
reference's are generated. Drawing them flat is what makes them look pasted on,
so they get the rounded corner and the leader line that the generated ones have.
"""

from __future__ import annotations

ACCENT = "&H003858E8"        # #E85838, ASS writes colours back to front
SHADOW = "&H80000000"        # half-transparent black, for lift without a stroke

TITLE_SPACING = 0.40         # measured off "수 문" and "김 포"
BRACKET = "「"


def _text_width(text: str, size: int, spacing: float) -> float:
    """Rough advance width. Korean is full width, latin and spaces are not."""
    width = 0.0
    for ch in text:
        if "가" <= ch <= "힣":
            width += size
        elif ch in " ":
            width += size * 0.32
        else:
            width += size * 0.55
    return width + spacing * max(len(text) - 1, 0)


def rounded_rect(w: float, h: float, r: float) -> str:
    """An ASS drawing of a rounded rectangle with its top left at the origin."""
    r = min(r, w / 2, h / 2)
    return (
        f"m {r:.0f} 0 "
        f"l {w - r:.0f} 0 b {w:.0f} 0 {w:.0f} 0 {w:.0f} {r:.0f} "
        f"l {w:.0f} {h - r:.0f} b {w:.0f} {h:.0f} {w:.0f} {h:.0f} {w - r:.0f} {h:.0f} "
        f"l {r:.0f} {h:.0f} b 0 {h:.0f} 0 {h:.0f} 0 {h - r:.0f} "
        f"l 0 {r:.0f} b 0 0 0 0 {r:.0f} 0"
    )


def title_events(item: dict, cx: int, cy: int, size: int, sub_size: int) -> list[str]:
    """A title: bracket ornament, the word itself, and an optional second line."""
    spacing = round(size * TITLE_SPACING)
    out = [
        f"{{\\an5\\pos({cx},{cy})\\fs{size}\\fsp{spacing}\\bord0\\shad4\\4c{SHADOW}"
        f"\\fad(200,200)}}{item['text']}"
    ]
    if item.get("bracket"):
        half = _text_width(item["text"], size, spacing) / 2
        out.append(
            f"{{\\an5\\pos({round(cx - half - size * 0.30)},{round(cy - size * 0.52)})"
            f"\\fs{round(size * 0.62)}\\bord0\\shad4\\4c{SHADOW}\\fad(200,200)}}{BRACKET}"
        )
    if item.get("sub"):
        out.append(
            f"{{\\an5\\pos({cx},{round(cy + size * 0.82)})\\fs{sub_size}\\fsp{round(sub_size * 0.10)}"
            f"\\bord0\\shad4\\4c{SHADOW}\\fad(200,200)}}{item['sub']}"
        )
    return out


def label_events(item: dict, cx: int, cy: int, size: int, width: int, height: int) -> list[str]:
    """A label: a rounded red plate, its text, and a leader line to what it names."""
    pad_x, pad_y = round(size * 0.55), round(size * 0.34)
    w = round(_text_width(item["text"], size, 0) + pad_x * 2)
    h = round(size * 1.05 + pad_y * 2)
    left, top = cx - w // 2, cy - h // 2

    events = []
    if item.get("to"):
        # the leader leaves the plate edge nearest the target, as the generated ones do
        tx, ty = round(width * item["to"][0]), round(height * item["to"][1])
        ax = min(max(tx, left + 12), left + w - 12)
        ay = top + h if ty > cy else top
        events.append(
            f"{{\\an7\\pos(0,0)\\bord0\\shad0\\1c{ACCENT}\\fad(200,200)\\p1}}"
            f"m {ax - 3} {ay} l {ax + 3} {ay} l {tx + 3} {ty} l {tx - 3} {ty}{{\\p0}}"
        )
        events.append(
            f"{{\\an7\\pos({tx - 9},{ty - 9})\\bord0\\shad0\\1c{ACCENT}\\fad(200,200)\\p1}}"
            f"m 9 0 b 18 0 18 18 9 18 b 0 18 0 0 9 0{{\\p0}}"
        )
    events.append(
        f"{{\\an7\\pos({left},{top})\\bord0\\shad0\\1c{ACCENT}\\fad(200,200)\\p1}}"
        f"{rounded_rect(w, h, size * 0.42)}{{\\p0}}"
    )
    events.append(
        f"{{\\an5\\pos({cx},{cy})\\fs{size}\\bord0\\shad0\\fad(200,200)}}{item['text']}"
    )
    return events


def number_events(item: dict, cx: int, cy: int, size: int) -> list[str]:
    """A dimension figure: the annotation red, never white, and no plate."""
    return [
        f"{{\\an5\\pos({cx},{cy})\\fs{size}\\bord2\\3c&H00000000\\shad0\\1c{ACCENT}"
        f"\\fad(200,200)}}{item['text']}"
    ]
