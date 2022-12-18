//main.ts
import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import { createPinia } from "pinia"
import App from "./App.vue";
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import "uno.css";
import { Icon } from "@iconify/vue";
import generatedRoutes from "virtual:generated-pages"
import { setupLayouts } from "virtual:generated-layouts";
import "@mdi/font/css/materialdesignicons.css";
const routes = setupLayouts(generatedRoutes);

const darkMode = {
  dark: true,
  colors: {
    primary: "#008080",
    secondary: "#7FFFD4",
    accent: "#000080",
    info: "#0c0c0c",
    success: "#44ff50",
    warning: "#FFD700",
    error: "#800040",
  }
}
const lightMode = {
  dark: false,
  colors: {
    primary: "#00f99d",
    secondary: "#fff4f4",
    accent: "#000fff",
    info: "#cccccc",
    success: "#00ff00",
    warning: "#ff9900",
    error: "#ff0000",
  }
}

createApp(App)
  .use(
    createRouter({
      history: createWebHistory(import.meta.env.BASE_URL),
      routes,
    })
  )
  .use(createPinia())
  .use(
    createVuetify({
      theme: {
        defaultTheme: "dark",
        themes: {
          dark: darkMode,
          light: lightMode,
        }
      },
      components,
      directives,
    })
  )
  .component("Icon", Icon)
  .mount("#app")