# UICLAP: Covers, Spines, Back Covers, and Flaps

## Core Rule

There is no universal UICLAP cover size. Obtain the official template in the
Portal after uploading the final interior file: trim size, final page count, and
paper determine the spine. Calculator values are only planning estimates; the
Portal cover-size guide and SVG are the production reference.

## Creative and Commercial Quality

Each book needs its own art direction, aligned with genre, thesis, audience,
and reading promise. Generative AI may create unique narrative base art, but it
must not copy third-party covers or identifiable artists' styles. Generate
textless base art; compose title, subtitle, author, back-cover copy, spine, QR
Code, and mandatory elements locally.

## Layout Planning

Without flaps, the external file is:

```text
bleed | back cover | spine | front cover | bleed
```

With `W` as closed-book width, `H` as closed-book height, and `S` as the
official Portal spine width:

```text
total width = W + S + W + 10 mm
total height = H + 10 mm
```

With two equal flaps of width `F`, the external file is:

```text
bleed | left flap | back cover | spine | front cover | right flap | bleed
total width = F + W + S + W + F + 10 mm
total height = H + 10 mm
```

These equations are planning aids only. Use the Portal template for production.
UICLAP lists flaps from 5 to 10 cm each, with 5, 7, and 10 cm options in its
editor. Use the matching flap template and confirm folds in the 3D preview.

## Production Rules

- Extend backgrounds 5 mm past every trim edge.
- Keep vital text and logos at least 10 mm inside the trim line.
- Reserve the Portal barcode area on the back cover; verify its exact placement
  in the generated template and preview.
- Upload one clean JPG external cover, up to 50 MB, at least 300 DPI; 600 DPI is
  the recommended target.
- Keep the cover file separate from the interior PDF.
- A printed spine requires at least 60 pages according to UICLAP. Confirm this
  before placing spine text.
- Validate alignment, folds, barcode reserve, logo behavior, and readability in
  the UICLAP 3D preview before marking a cover upload-ready.

## Official Sources Consulted on 2026-07-21

- [Cover: format, file type, and material](https://suporte.uiclap.com/support/solutions/articles/67000705782-capa-formato-tipo-de-arquivo-e-material)
- [From interior file to template, bleed, and safety margin](https://suporte.uiclap.com/support/solutions/articles/67000747899-capa-do-miolo-ao-gabarito-com-sangria-e-margem-de-seguranca)
- [Cover upload](https://suporte.uiclap.com/support/solutions/articles/67000705794-upload-da-capa)
- [How to create and publish a cover with flaps](https://suporte.uiclap.com/support/solutions/articles/67000556802-como-fazer-e-publicar-a-capa-com-orelha-tutorial-)
