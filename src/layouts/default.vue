<script setup lang="ts">
const items = reactive([
    { title: 'Home', icon: 'mdi-home', to: '/' },
    { title: 'About', icon: 'mdi-account', to: '/about' },
    { title: 'Contact', icon: 'mdi-phone', to: '/contact' },
    { title: 'Login', icon: 'mdi-login', to: '/login' },
    { title: 'Register', icon: 'mdi-account-plus', to: '/register' },
  ])
const drawer = ref(false)
const response = ref(null)
const fetchResponse = async () => {
  const res = await fetch('/api')
  response.value = await res.json()
}
onMounted(fetchResponse)
</script>
<template>
    <v-navigation-drawer
        app
        v-model="drawer"
        dense
        >
      <v-list dense>
        <v-list-item link v-for="item in items" :key="item.title">
            <RouterLink :to="item.to" exact row>
            <v-icon mx-2>{{ item.icon }}</v-icon>
            <v-list-item-title> {{ item.title }}</v-list-item-title>
            </RouterLink>
          </v-list-item>
        </v-list>
        </v-navigation-drawer>
    <v-app-bar
        app
        color="primary"
        dark
        >
        <v-app-bar-nav-icon
        @click.stop="drawer = !drawer"
        ></v-app-bar-nav-icon>
        <v-toolbar-title>   {{response}}</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon>
            <v-icon>mdi-magnify</v-icon>
        </v-btn>
        <v-btn icon>
            <v-icon>mdi-heart</v-icon>
        </v-btn>
        <v-btn icon>
            <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>
    </v-app-bar>
    <v-main>
        <RouterView />
    </v-main>
    <TheFooter />
</template>