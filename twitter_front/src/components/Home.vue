<template>
  <div class="nav">
    <article class="border p-2 ${animation}">
        <span class="float-right"><em>${post.timestamp}</em></span>
        <span><img src="${post.image}" style="width: 40px; height: 40px;" class="rounded-circle"><a href="/profile/${post.username}"><strong class="text-primary ml-3">${post.username}</strong></a></span>
        <p id="content-${post.id}" style="white-space: pre-line;">
            ${post.content}
    </p>
  </div>
</template>

<script>
export default {
  name: 'Home',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.nav {
  background-color:deepskyblue;
  padding: 10px;
}
.nav > h2 {
  color:white;
  text-decoration: bold;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>