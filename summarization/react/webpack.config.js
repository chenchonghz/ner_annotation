var path = require('path');

module.exports = {
  entry: "./js/app.jsx",
  output: {
    path: path.join(__dirname, "js"),
    filename: "bundle.js"
  },
  resolve: {
    extensions: ['', '.js', '.jsx', '.scss'],
    modulesDirectories: ['js', 'node_modules', 'css']
  },
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loader: 'babel-loader?optional=runtime'
      },
      {
        test: /\.css$/,
        loader: "style!css"
      },
      {
        test: /\.scss$/,
        loader: 'style!css!sass'
      }
    ]
  }
};