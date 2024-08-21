var path = require('path');
module.exports = {
    mode: 'development',
    // webpack folder’s entry js — excluded from jekll’s build process.
    entry: path.resolve("./assets/webpack/entry.js"),
    output: {
      // we’re going to put the generated file in the assets folder so jekyll will grab it.
      // if using GitHub Pages, use the following:
      // path: "assets/javascripts"
      path: path.resolve(__dirname, "assets/js/"),
      filename: "bundle.js"
    },
    module: {
     rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      }
    ]
    }
  };