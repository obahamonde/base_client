import {
  defineConfig,
  presetAttributify,
  presetIcons,
  presetUno,
  presetWebFonts,
  // transformerDirectives,
  // transformerVariantGroup,
} from 'unocss'

export default defineConfig({
  shortcuts: [
  ['row', 'flex flex-row'],
  ['col', 'flex flex-col'],
  ['center', 'items-center justify-center'],
  ['middle', 'items-center'],
  ['between', 'justify-between'],
  ['around', 'justify-around'],
  ['evenly', 'justify-evenly'],
  ['auto', 'flex-auto'],
  ['start', 'flex-start'],
  ['end', 'flex-end'],
  ['scale', 'scale-105 duration-200 ease-in-out transition-all'],
  ['shadow', 'shadow-md shadow-gray-500'],
  ],
  presets: [
    presetUno(),
    presetAttributify(),
    presetIcons({
      scale: 1.2,
      warn: true,
    }),
    presetWebFonts({
      fonts: {
        sans: 'DM Sans',
        serif: 'DM Serif Display',
        mono: 'DM Mono',
      },
    }),
  ],
  // transformers: [
  //   transformerDirectives(),
  //   transformerVariantGroup(),
  // ],
})
