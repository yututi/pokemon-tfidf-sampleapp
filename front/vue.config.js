module.exports = {
    publicPath:'/',
    outputDir:'../server/static/',
    assetsDir:'assets',
    pages: {
        index: {
            entry: 'src/main.ts', // エントリーポイントとなるjs
            template: 'public/index.html', // テンプレートのHTML
            filename: 'index.html' // build時に出力されるファイル名
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