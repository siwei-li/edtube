<template>
<div class="searchBox">
  <el-autocomplete placeholder="Search..." v-model="query"
                   :fetch-suggestions="querySearchAsync" @select="handleSelect" @keyup.enter.native="search"
                   :trigger-on-focus="false"
                   class="front-search">
    <el-button class="search-button" slot="append" icon="el-icon-search" @click="search"></el-button>
  </el-autocomplete>
</div>
</template>

<script>
export default {
  name: "Search",
  data() {
    return {
      query: "",
      queryList: [],
    }
  },
  methods: {

    querySearchAsync(queryString, cb) {

      var results = queryString ? this.queryList.filter(this.createStateFilter(queryString)) : this.queryList;

      clearTimeout(this.timeout);
      this.timeout = setTimeout(() => {
        cb(results);
      }, 3000 * Math.random());
    },

    createStateFilter(queryString) {
      return (query) => {
        return (query.value.toLowerCase().indexOf(queryString.toLowerCase()) === -1);
      };
    },

    handleSelect(item) {
      console.log(item);
      this.query = item;
    },

    search() {
      if (!query) {
        return;
      }

    }
  }
}
</script>

<style>
.front-search {
  width: 400px;
  /*width: auto;*/
}
</style>