const path = require('path');

module.exports = {
  entry: './static/js/components/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'static/js/dist'),
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react']
          }
        }
      }
    ]
  },
  resolve: {
    extensions: ['.js', '.jsx']
  }
};