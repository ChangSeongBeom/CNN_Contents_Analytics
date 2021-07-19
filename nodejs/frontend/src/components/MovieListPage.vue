<template> 
    <div class="movies"> 
        <h1>영화 목록</h1> 
        <div class="container"> 
            <div class="outer">
                 <div class="inner">
                      <div class="centered" v-for="movie in movies" :key="movie.id">
                           <img v-bind:src="movie.poster" class="poster"> 
                           <div> <strong>{{movie.name}}</strong> - <i>{{movie.director}}</i> 
                           [{{movie.year}}] 
                           <router-link :to="{ name: 'detailmovie', params: { id: movie.id }}">더보기</router-link> 
                           </div>
                     </div> 
                </div> 
            </div> 
        </div> 
    </div> 
</template>

<script> /* eslint-disable */ 
export default { 
    created() { 
        this.$http.get("/movies").then(response => { 
            this.movies = response.data; 
            }); 
        }, 
        data() { 
            return { 
                movies: [] 
            };
        } 
    }; 
</script>

