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
const { state, dispatch } = useStore()
const drawerRight = ref(false)
const valid = ref(true)
const name = ref("")
const code = ref("")
const isRegistered = ref(false)
const passwordRules = ref([
  (v: any) => !!v || 'Password is required',
  // password must contain at least 1 lowercase, 1 uppercase, 1 number annd 1 symbol
  (v: string) => /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}/.test(v) || 'Password must be valid (8 characters, 1 lowercase, 1 uppercase, 1 number annd 1 symbol'
])
const email = ref("")
const emailRules = ref([
  (v: any) => !!v || 'E-mail is required',
  (v: string) => /.+@.+\..+/.test(v) || 'E-mail must be valid',
])

const signup = async () => {
  const formdata = new FormData();
  formdata.append('username',email.value)
  formdata.append('password',name.value)
  const { data } = await useFetch('/api/register', {
    method: 'POST',
    body: formdata
  }).json()
  const { message } = unref(data)
  alert(message)
  isRegistered.value = true

}

const verify = async () => {
  const { data } = await useFetch(`/api/register/${email.value}/${code.value}`).json()
  const { message } = unref(data)
  alert(message)
}

const signin = async () => {
  const formdata = new FormData();
  formdata.append('username',email.value)
  formdata.append('password',name.value)
  const { data } = await useFetch('/api/token', {
    method: 'POST',
    body: formdata
  }).json()
  const tokenInfo = unref(data)
  dispatch({token: tokenInfo["AccessToken"]})
  alert(tokenInfo["AccessToken"])
  const { data: user } = await useFetch('/api/user_info',{
    headers: {
        "Authorization": `Bearer ${tokenInfo["AccessToken"]}`
    }
  }).json()
  dispatch({userInfo: unref(user)})
  }
</script>
<template>
  <v-navigation-drawer app v-model="drawer" dense>
    <v-list dense>
      <v-list-item link v-for="item in items" :key="item.title">
        <RouterLink :to="item.to" exact row decoration-none>
          <v-icon mx-2>{{ item.icon }}</v-icon>
          <v-list-item-title> {{ item.title }}</v-list-item-title>
        </RouterLink>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
  <v-app-bar app color="primary" dark>
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    <v-toolbar-title> {{ response }}</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn icon @click="toggleDark()">
      <v-icon>{{ $vuetify.theme.current.dark ? 'mdi-lightbulb-off' : 'mdi-lightbulb-on' }}</v-icon>
    </v-btn>
    <Auth @login="drawerRight = !drawerRight" />
  </v-app-bar>
  <v-main>
    <RouterView />
  </v-main>
  <v-navigation-drawer app v-model="drawerRight" location="right">
    <v-form ref="form" v-model="valid" lazy-validation v-if="!state.userInfo">
      <v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>
      <v-text-field v-model="name" :counter="8" :rules="passwordRules" label="Password" required type="password"></v-text-field>
      <v-text-field v-if="isRegistered" v-model="code" label="Code"></v-text-field>
      <v-btn color="success" v-if="!isRegistered" class="m-4" @click="signup()">
        Sign Up
      </v-btn>
      <v-btn v-if="isRegistered" color="primary" class="mr-4" @click="verify()">
          Sign In
        </v-btn>
      <v-btn color="primary" class="mr-4" @click="signin()">
        Sign In
      </v-btn>

    </v-form>
    <v-card v-else>
      <v-card-title>
        <span class="headline">{{ state.userInfo["email"] }}</span>
      </v-card-title>
      </v-card>
  </v-navigation-drawer>
</template>
