module.exports = {
    devServer: {
      proxy: {
        "^/api": {
          target: "http://192.168.52.20:8000"
        }
      }
    }
  };