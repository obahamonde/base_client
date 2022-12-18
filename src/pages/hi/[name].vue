<script setup lang="ts">
const props = defineProps<{ name: string }>()
const router = useRouter()
const response = ref(null)
onMounted(async() => {
  const { data } = await useFetch("/api/").json()
  response.value = unref(data) as any
})
  </script>

<template>
  <div>
    <Icon icon="simple-icons:fastapi" color="#008080" />
    <p>
      Hi, {{ props.name }}
    </p>
    <div>
      <p>
        {{ response }}
      </p>
      <button
        class="btn m-3 text-sm mt-8"
        @click="router.back()"
      >
        Back
      </button>
    </div>
  </div>
</template>
