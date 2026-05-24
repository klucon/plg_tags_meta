from __future__ import annotations

from html import escape

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.hooks import hooks
from src.database.models.plugin import InstalledPlugin

PLUGIN_NAME = "plg_tags_meta"


def setup(registry: object) -> None:
    hooks.on("frontend.head", render_head)


async def _settings(db: AsyncSession | None) -> dict[str, object]:
    if db is None:
        return {}
    plugin = (
        await db.execute(select(InstalledPlugin).where(InstalledPlugin.name == PLUGIN_NAME))
    ).scalar_one_or_none()
    return plugin.settings if plugin and isinstance(plugin.settings, dict) else {}


def _page_url(request: object) -> str:
    raw = str(getattr(request, "url", "") or "")
    return raw.split("?", 1)[0].split("#", 1)[0]


async def render_head(
    *,
    request: object,
    db: AsyncSession | None = None,
    site_description: str = "",
    **kwargs: object,
) -> str:
    settings = await _settings(db)
    description = str(settings.get("description") or "").strip()
    robots = str(settings.get("robots") or "index,follow").strip()
    canonical = str(settings.get("canonical") or "auto").strip()

    tags: list[str] = []
    if description and description != site_description:
        tags.append(f'<meta name="description" content="{escape(description, quote=True)}">')
    if robots:
        tags.append(f'<meta name="robots" content="{escape(robots, quote=True)}">')
    if canonical == "auto":
        tags.append(f'<link rel="canonical" href="{escape(_page_url(request), quote=True)}">')
    elif canonical.startswith(("http://", "https://")):
        tags.append(f'<link rel="canonical" href="{escape(canonical, quote=True)}">')
    return "".join(tags)
