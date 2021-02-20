<template>
<div class="searchBox">
  <el-autocomplete placeholder="Enter something that interests you!"
                   v-model="query"
                   :fetch-suggestions="querySearchAsync" @select="handleSelect" @keyup.enter.native="search"
                   :trigger-on-focus="false"
                   popper-class="popover"
                   class="front-search">
    <template slot-scope="{ item }">
      <div class="title">{{ item.value }}</div>
      <span class="category">{{ item.category }}</span>
    </template>
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
    load() {
      return [
        {"value": "vid1", "category": "Math"},
        {"value": "vid2", "category": "Arts"},
      ]
    },
    querySearchAsync(query, cb) {
      var videos = this.queryList;
      var results = query ? videos.filter(this.createStateFilter(query)) : videos;

      clearTimeout(this.timeout);
      this.timeout = setTimeout(() => {
        cb(results);
      }, 3000 * Math.random());
    },

    createStateFilter(query) {
      return (item) => {
        return (item.value.toLowerCase().indexOf(query.toLowerCase()) === 0);
        // return true;
      };
    },

    handleSelect(item) {
      console.log(item.value);
      this.query = item.value;
    },

    search() {
      if (!query) {
        return;
      }

    }
  },
  mounted() {
    this.queryList = this.load();
  }
}
</script>

<style lang="less">
.front-search {
  //max-width: 500px;
  width: 400px;
}

.popover {
  //width: 500px;
  line-height: normal;
  padding: 7px;

  .title {
    text-overflow: ellipsis;
    overflow: hidden;
  }

  .category {
    font-size: 12px;
    color: #b4b4b4;
  }

  .highlighted .category {
    color: #ddd;
  }
}
</style>