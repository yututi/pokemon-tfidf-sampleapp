module.exports = {
    publicPath:'/',
    outputDir:'../back/web/',
    assetsDir:'assets',
    pages: {
        index: {
            entry: 'src/main.ts',
            template: 'public/index.html',
            filename: 'pokemon.html'
        }
    },
    devServer: {
        historyApiFallback: {
            rewrites: [
                { from: /\//, to: '/pokemon.html' },
            ]
        }
    }
}