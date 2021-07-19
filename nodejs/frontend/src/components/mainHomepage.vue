<template>
    <div id>
        <p>sfsf</p>
    </div>
</template>


<script>
export default {
  created: function () {
    var id = this.$route.params.id;
    this.$http.get('http://localhost:3000/users')
        .then((response) => {
          this.movie = response.data[0]
        })
  },
  data: function () {
    return {
      movie: {}
    }
  }
}
</script>