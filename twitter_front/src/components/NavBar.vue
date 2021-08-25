<template>
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <router-link to="/" class="navbar-brand">Poor Man's Twitter</router-link>
      <div class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link to="/tweets" class="nav-link">Tweets</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/post" class="nav-link">Post</router-link>
        </li>
      </div>
    </nav>
</template>

<script>
export default {
  name: 'NavBar'
}
</script>

<style>
nav {
  margin-bottom: 20px;
}

</style>

