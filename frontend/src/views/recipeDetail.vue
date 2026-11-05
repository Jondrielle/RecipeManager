<script setup>
import { useRoute, useRouter } from 'vue-router'

const router = useRouter()
const route = useRoute()

</script>

<template>
    <div>
        <h1>Recipe Detail Page </h1>
        <p>Recipe ID: {{ route.params.id }}</p>
    </div>
</template>

<style scoped>

</style>