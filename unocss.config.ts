import {
  defineConfig,
  presetAttributify,
  presetIcons,
  presetTypography,
  presetUno,
  presetWebFonts,
  transformerDirectives,
  transformerVariantGroup,
} from "unocss";

export default defineConfig({
  shortcuts: [
    ["scale", "hover:scale-110 hover:transition-all duration-200 ease-in-out"],
    ["cp", "cursor-pointer"],
    ["rf", "rounded-full"],
    ["col", "flex flex-col"],
    ["row", "flex flex-row"],
    ["center", "items-center justify-center"],
    ["start", "items-start justify-start"],
    ["end", "items-end justify-end"],
    ["tr", "top-0 right-0"],
    ["br", "bottom-0 right-0"],
    ["bl", "bottom-0 left-0"],
    ["tl", "top-0 left-0"],
    ["sh", "shadow-gray-500 shadow-md"],
    ["sh-sm", "shadow-sm"],
    ["sh-md", "shadow-md"],
    ["sh-lg", "shadow-lg"],
    ["sh-xl", "shadow-xl"],
    ["sh-2xl", "shadow-2xl"],
    ["scale", "hover:scale-110 hover:transition-all duration-200 ease-in-out"],
    ["grid2", "grid grid-cols-2"],
    ["grid3", "grid grid-cols-3"],
    ["grid4", "grid grid-cols-4"],
    ["grid5", "grid grid-cols-5"],
    ["grid6", "grid grid-cols-6"],
    ["slide-up", "animate-slide-in-up animate-duration-200"],
    ["slide-down", "animate-slide-in-down animate-duration-200"],
    ["slide-left", "animate-slide-in-left animate-duration-200"],
    ["slide-right", "animate-slide-in-right animate-duration-200"],
    ["fade-in", "animate-fade-in animate-duration-200"],
    ["fade-in-up", "animate-fade-in-up animate-duration-200"],
    ["fade-in-down", "animate-fade-in-down animate-duration-200"],
    ["fade-in-left", "animate-fade-in-left animate-duration-200"],
    ["fade-in-right", "animate-fade-in-right animate-duration-200"],
    ["spin-in-up", "animate-spin-in-up animate-duration-200"],
    ["spin-in-down", "animate-spin-in-down animate-duration-200"],
    ["spin-in-left", "animate-spin-in-left animate-duration-200"],
    ["spin-in-right", "animate-spin-in-right animate-duration-200"],
    ["no-outline", "outline-none focus:outline-none hover:outline-none"],
    ["toast", " tr mt-16 row rounded-lg  shadow-primary sh-lg z-50 fixed p-4"],
    ],
  presets: [
    presetUno(),
    presetAttributify(),
    presetIcons({
      scale: 1.2,
      warn: true,
    }),
    presetTypography(),
    presetWebFonts({
      fonts: {
        sans: "Inter",
        serif: "Alegreya",
        mono: "DM Mono",
        script: "Merienda",
      },
    }),
  ],
  transformers: [transformerDirectives(), transformerVariantGroup()],
  safelist: "prose prose-sm m-auto text-left".split(" "),
  rules: [
    [
      /^x(\d+)$/,
      ([, d]) => ({
        height: `${d}rem`,
        width: `${d}rem`,
      }),
    ],
     ],
});
