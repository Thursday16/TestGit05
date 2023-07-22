<template>
  <div>
      <header class="shadow-sm bg-white">
          <nav class="container mx-auto p-4 flex justify-between">
              <NuxtLink to="/" class="font-bold">Blackpink</NuxtLink>
              <ul class="flex gap-4">
                  <li><NuxtLink to="/">Home</NuxtLink></li>
                  <li><NuxtLink to="/jennie" class="btn">Jennie</NuxtLink></li>
                  <li><NuxtLink to="/lisa" class="btn">Lisa</NuxtLink></li>
                  <li><NuxtLink to="/rose" class="btn">Rose</NuxtLink></li>
                  <li><NuxtLink to="/jisoo" class="btn">Jisoo</NuxtLink></li>
              </ul>
          </nav>
      </header>

      <!-- page content go here -->
      <div class="container mx-auto p-4">
          <slot />
      </div>
  </div>
</template>

<style scoped>
  .router-link-exact-active {
      color: #000;
  }
</style>