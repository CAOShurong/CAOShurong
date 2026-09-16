# Profile presentation decisions

## Current direction, 16 September 2026

- GitHub foregrounds what the owner builds and the technical problems they solve. The academic website covers EE research and the broader personal background.
- Keep a brief academic introduction, followed by selected working projects and specific accepted upstream contributions. Place the compact research background after these sections.
- Preserve the English display name **ShurongCAO** and the warm homepage banner. Use native GitHub typography and compact tables below it.
- Show ability through concrete work. Omit achievement panels, logo walls, badge rankings, and self-assessed capability lists from the README.
- Link to live external PR searches with `-user:CAOShurong`, separating merged and open work. Do not hard-code changing contribution totals into the profile.
- Keep the existing manifest and contribution log as a dated archive. Validate recorded merges while allowing newer accepted work.
- Earlier graphic decisions below remain historical context; achievement and ecosystem assets are retained but no longer displayed.

## Earlier direction

Owner direction, 13 September 2026. Preserve these choices during future content or contribution updates:

- The profile introduction and banners are English only. Display the name exactly as **ShurongCAO**: no spaces, uppercase CAO. This does not rename the GitHub account handle `CAOShurong` or change publication citations elsewhere.
- Use one warm beige orbital banner at the top. Include **View my homepage** inside it and link the whole image to https://caoshurong.github.io/.
- Do not restore the separate purple website-link banner, bilingual heading, or redundant homepage text link above the banner.
- Achievement and ecosystem graphics use white/warm near-white backgrounds, dark readable text, subtle borders and muted accents. Do not restore the black panels.
- Keep substantive contribution updates separate from styling. Do not overwrite these SVGs with older generated copies when refreshing metrics.

Files: README.md, assets/banner.svg, assets/achievements.svg, assets/ecosystem-matrix.svg. The unused assets/website-link.svg remains available in history/source but is not displayed.

GitHub caches SVGs aggressively. README artwork URLs are pinned to the artwork commit. After changing these SVGs, commit them first and update README image URLs to that new commit so visitors receive the intended images.
