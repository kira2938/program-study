var Map = function (startX, startY, tileWidth, tileHeight, wallFillStyle) {
    // キャンパス上での描画開始位置
    this.startX = startX;
    this.startY = startY;

    // タイルの大きさ
    this.tileSize = {'w': tileWidth, 'h': tileHeight};

    this.wallFillStyle=  wallFillStyle; // タイルの塗りつぶし方法

    // マップ
    this.map = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,0,1,1,1,1,1,1,1,0,1,1,1,0],
        [0,1,1,1,0,1,0,1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1,1,1,1,1,0,1,0],
        [0,1,1,1,1,1,1,1,0,0,1,0,1,1,0],
        [0,1,0,0,1,0,0,1,0,0,1,0,1,0,0],
        [0,1,1,1,1,0,0,1,1,1,1,1,1,1,0],
        [0,1,0,0,1,0,0,1,0,1,0,1,0,1,0],
        [0,1,1,1,1,1,1,1,0,1,0,1,0,1,0],
        [0,0,1,0,0,1,0,1,0,1,0,1,0,1,0],
        [0,0,1,0,0,1,0,1,0,1,0,1,0,1,0],
        [0,0,1,1,1,1,1,1,1,1,0,1,0,1,0],
        [0,0,0,1,0,0,0,0,0,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ];
};

Map.prototype = {
    // タイルの行数
    getRowLength: function() {
        return this.map.length;
    },

    // タイルの列数
    getColLength: function() {
        return this.map[0].length;
    },

    // タイルの幅
    getTileWidth : function() {
        return this.tileSize.w;
    },

    // タイルの高さ
    getTileHeight : function() {
        return this.tileSize.h;
    },

    // ピクセルで表される座標の点(x, y)が含まれるタイルを返す
    getTile : function(x, y) {
        var col = Math.floor((x - this.startX) / this.getTileWidth());
        var row = Math.floor((y - this.startY) / this.getTileHeight());
        return {'row': row, 'col': col, 'kind': this.map[row][col]};
    },

    // row行col列目のタイルのピクセルで表される座標の左上の点(x, y)を返す
    getTileLeftTop : function(row, col) {
        return {'left': this.startX + col * this.getTileWidth(), 'top': this.startY + row * this.getTileHeight()};
    },

    // ピクセル座標 (x, y) が属しているタイルの中心座標を返す
    getTileCenter : function(x, y) {
        var tile = this.getTile(x, y);
        var leftTop = this.getTileLeftTop(tile.row, tile.col);
        return {
            'x': Math.floor(leftTop.left + this.getTileWidth() / 2),
            'y': Math.floor(leftTop.top + this.getTileHeight() / 2)
        };
    },

    // ピクセルで表される座標の点(x, y)が属するタイルの左のタイルが壁であれば true を返す。
    isLeftBlockWall : function(x, y) {
        var tile = this.getTile(x, y);
        return tile.col == 0 || this.map[tile.row][tile.col - 1] == 0;
    },

    // ピクセルで表される座標の点(x, y)が属するタイルの上のタイルが壁であれば true を返す。
    isAboveBlockWall : function(x, y) {
        var tile = this.getTile(x, y);
        return tile.row == 0 || this.map[tile.row - 1][tile.col] == 0;
    },

    // ピクセルで表される座標の点(x, y)が属するタイルの右のタイルが壁であれば true を返す。
    isRightBlockWall : function(x, y) {
        var tile = this.getTile(x, y);
        return tile.col + 1 == this.getColLength() || this.map[tile.row][tile.col + 1] == 0;
    },

    // ピクセルで表される座標の点(x, y)が属するタイルの下のタイルが壁であれば true を返す。
    isBelowBlockWall : function(x, y) {
        var tile = this.getTile(x, y);
        return tile.row + 1 == this.getRowLength || this.map[tile.row + 1][tile.col] == 0;
    },

    // 壁の描画
    drawWall : function(ctx, row, col) {
        ctx.fillStyle = this.wallFillStyle;
        ctx.rect(this.startX + col * this.getTileWidth(), this.startY + row * this.getTileHeight(),
            this.getTileWidth(), this.getTileHeight());
        ctx.fill();
    },

    // クッキーの描画
    drawCookie : function(ctx, i, j) {

    },

    // マップを描画
    draw : function(ctx) {
        ctx.beginPath();
        for(var j = 0; j < this.getRowLength(); j++) {
            for( var i = 0; i < this.getColLength(); i++) {
                if(this.map[j][i] == 0) {
                    this.drawWall(ctx, j, i);
                } else if (this.map[j][i] == 2 ){
                    this.drawCookie(ctx, j, i);
                }
            }
        }
    }
};
