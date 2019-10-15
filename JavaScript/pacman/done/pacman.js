// パックマンの属性とともにコンストラクタを定義してPacmanという名前をつける
var Pacman = function(radius, speed, theta, map, row, col) {
  // タイルベースの移動に必要な情報
  this.map = map;

  var rect = this.map.getTilePosition(row, col);

  // ぷくセルベースの移動の描画に必要な情報
  this.radius = radius;
  this.position = {
    x: Math.floor(rect.left + this.map.getTileWidth() / 2),
    y: Math.floor(rect.top + this.map.getTileHeight() / 2)
  };
  this.moveingDirection = { x: 0, y: 0 };
  this.speed = speed;
  this.theta = theta;
  this.dTheta = 3;
};
// パックマンのメソッドを定義
// 今のところ、メソッドはコンストラクタの持つporototypeオブジェクトのメソッドとして定義すると覚える
Pacman.prototype = {
  getCx: function() {
    return this.position.x;
  },

  getCy: function() {
    return this.position.y;
  },

  getRadius: function() {
    return this.radius;
  },

  goLeft: function() {
    return this.getCx() - this.getRadius;
  },

  goRight: function() {
    return this.getCx() + this.getRadius;
  },

  goTop: function() {
    return this.getCy() - this.getRadius;
  },

  goBottom: function() {
    return this.getCy() + this.getRadius;
  },

  getSpeed: function() {
    return this.speed;
  },

  getTheta: function() {
    return this.theta;
  },

  goLeft: function() {
    this.moveingDirection = { x: -1, y: 0 };
  },

  goRight: function() {
    this.moveingDirection = { x: 1, y: 0 };
  },

  goUp: function() {
    this.moveingDirection = { x: 0, y: -1 };
  },

  goDown: function() {
    this.moveingDirection = { x: 0, y: 1 };
  },

  move: function() {
    this.chew();

    var previous_pos_x = this.position.x;
    var previous_pos_y = this.position.y;

    this.position.x +=
      (this.moveingDirection.x * duration * this.getSpeed()) / 1000;

    if (this.isInWall()) {
      this.position.x = previous_pos_x;
    }

    this.position.y +=
      (this.moveingDirection.y * duration * this.getSpeed()) / 1000;

    if (this.isInWall()) {
      this.position.y = previous_pos_y;
    }

    // for (var i = 0; i < 2; i++) {
    //   this.position[i] += this.moveingDirection[i];
    // }
  },

  chew: function() {
    if (this.theta >= 30 || this.theta <= 0) {
      this.dTheta *= -1;
    }
    this.theta += this.dTheta;
    return this.theta;
  },

  draw: function(ctx) {
    // RADIUS = 20;
    ctx.strokeStyle = "#FF0000";
    ctx.fillStyle = "#FF0000";
    ctx.beginPath();
    ctx.arc(
      this.getCx(),
      this.getCy(),
      this.radius,
      (this.getTheta() * Math.PI) / 180,
      ((360 - this.getTheta()) * Math.PI) / 180
    );
    ctx.lineTo(this.getCx(), this.getCy());
    ctx.lineTo(
      this.getCx() + this.radius * Math.cos((this.getTheta() * Math.PI) / 180),
      this.position[1] +
        this.radius * Math.sin((this.getTheta() * Math.PI) / 180)
    );
    ctx.fill();
  }
};
