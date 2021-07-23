<template>
  <header>
  <h1>경영지원시스템팀</h1>
 
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
  background-color: white;

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
#app > header > nav > ul > li:nth-child(1) > a{
  color:white;
}
#app > header > nav > ul > li:nth-child(2) > a{
    color:white;

}
#app > header > nav > ul > li:nth-child(3) > a{
  color:white;
}
</style>