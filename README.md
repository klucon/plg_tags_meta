# plg_tags_meta

Plugin pro generování canonical a volitelné meta description podle nastavení tagů.

## Metadata

| Pole | Hodnota |
| :--- | :--- |
| Typ | `plugin` |
| Verze | `0.1.6` |
| Vendor | `klucon` |
| Extension ID | `klucon/plg_tags_meta` |
| Kategorie | `seo` |
| Licence | MIT |
| Core minimum | `0.2.15` |
| Python | `>=3.12` |
| Entry point | `src.plugins.plg_tags_meta` |
| Repository | `https://github.com/klucon/plg_tags_meta` |
| Admin URL | `-` |

## Účel

Tagy - Meta SEO je marketplace rozšíření pro KLUCON CMS. Balíček je určený pro instalaci přes `/admin/marketplace` a musí projít validací manifestu, checksumu a podpisu.

## Struktura

```text
src/**/plg_tags_meta/
├── manifest.json
├── __init__.py
├── i18n/
└── ...
```

Manifest používá schema `1.0`, deklaruje typ `plugin`, kompatibilitu s core, i18n doménu `plg_tags_meta` a bezpečnostní capabilities. Implementace obsahuje hook handlery.

## Balíčkování

Release ZIP se staví z `src/**/plg_tags_meta/manifest.json` pomocí GitHub Actions workflow `.github/workflows/release-package.yml`. Do balíčku nepatří cache, `.git`, lokální ZIP artefakty ani dočasné soubory.

## Instalace

1. Publikuj ZIP a metadata do marketplace serveru.
2. V CMS otevři `/admin/marketplace`.
3. Vyber `plg_tags_meta` a instaluj verzi `0.1.6`.
4. Po instalaci ověř záznam v příslušné tabulce `installed_*`.

## Poznámky k verzi

Robots meta tag byl odstraněn z tohoto pluginu; patří do samostatného nastavitelného pluginu.
