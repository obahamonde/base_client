<template>
 <v-app
  app
 >
 <v-main app>
    <RouterView />
</v-main>
</v-app>
</template>
<style global>
html,
body,
#app {
  height: 100%;
  margin: 0;
  padding: 0;
}

html.dark {
  background: #121212;
}

</style>