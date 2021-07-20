<template>
    <div>
        parameter : {{param}}
    </div>
</template>

<script>

export default {
    name:'Detailview',
    computed: {
        param: function () {
            return this.$route.params;
        }
    }
}
</script>
