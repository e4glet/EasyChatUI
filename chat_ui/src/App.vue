<template>
  <router-view v-wechat-title="$route.meta.title" />
</template>

<style>
body {
  padding: 0;
  margin: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}



:root {
  --dsr-input-bg: rgb(243, 244, 246);
  --dsr-input-border: #dce0e9;
  --ds-input-chat-color: rgb(64, 64, 64);
}

</style>
