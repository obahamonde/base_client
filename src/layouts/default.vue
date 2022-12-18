import { useRequest } from '../hooks/request';
<script setup lang="ts">
import { useRequest } from '~/hooks';
import { useTheme } from 'vuetify';
const items = reactive([
    { title: 'Home', icon: 'mdi-home', to: '/' },
    { title: 'About', icon: 'mdi-account', to: '/about' },
    { title: 'Contact', icon: 'mdi-email', to: '/contact' }
  ])
const drawer = ref(false)
const { response } = useRequest("/api")
const theme = useTheme();
const toggleDark = () => {
    theme.global.name.value = theme.global.name.value === 'light' ? 'dark' : 'light';
  };
</script>
<template>
    <v-navigation-drawer
        app
        v-model="drawer"
        dense
        >
      <v-list dense>
        <v-list-item link v-for="item in items" :key="item.title">
            <RouterLink :to="item.to" exact row decoration-none>
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
        <v-btn icon
          @click="toggleDark()"
        >
            <v-icon>{{ $vuetify.theme.current.dark ? 'mdi-lightbulb-off' : 'mdi-lightbulb-on' }}</v-icon>
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