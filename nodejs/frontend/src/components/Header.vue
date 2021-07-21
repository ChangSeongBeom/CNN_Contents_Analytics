<template>
  <header>
  <h1>Hyundai Autoever EDU WG RnD</h1>
  <nav>
    <ul>
      <li><a href="#" router-link class="menu" to="/"> 1</a></li>
      <li><a href="#" router-link class="menu" to="/">메뉴 2</a></li>
      <li><a href="#" router-link class="menu" to="/">메뉴 3</a></li>
    </ul>
  </nav>
  </header>
 
</template>

<script>
export default {
}
</script>

<style>
header {
  display: grid;
  grid-auto-flow: column;
  grid-template-columns: 1fr;
}

h1 {
  display: inline-block;
  text-align: left;
  vertical-align: left;
  color: white;
  margin: 0.5rem;
  padding: 0;
}

nav {
  display: inline-block;
  vertical-align: middle;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
}

li.icon {
  flex-basis: 25%;
}

header {
  background: cadetblue;
  padding: 20px;
}

a {
  display: block;
  text-align: center;
  margin: .25rem;
  padding: .5rem 1rem;
  text-decoration: none;
  font-weight: bold;
  color: white;
  background: teal;
}

a:hover {
  background: yellowgreen;
}

html {
  box-sizing: border-box;
}

*, *:before, *:after {
  box-sizing: inherit;
}
</style>