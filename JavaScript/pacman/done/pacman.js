// パックマンの属性とともにコンストラクタを定義してPacmanという名前をつける
var Pacman = function(cx, cy, speed, theta) {
  this.position = [cx, cy];
  this.moveingDirection = [0, 0];
  this.speed = speed;
  this.theta = theta;
};

// 定義したPacmanコンストラクタにメソッドを定義
Pacman.prototype = {
  getCx: function() {
    return this.position[0];
  },

  getCy: function() {
    return this.position[1];
  },

  getPosition: function(i) {
    return this.position[i];
  },

  getSpeed: function() {
    return this.speed;
  },

  getTheta: function() {
    return this.theta;
  },

  go_left: function() {
    this.movineDirection = [-1 * this.getSpeed(), 0];
  },

  go_right: function() {
    this.movineDirection = [this.getSpeed(), 0];
  },

  go_up: function() {
    this.movineDirection = [0, -1 * this.getSpeed()];
  },

  go_down: function() {
    this.movineDirection = [0, this.getSpeed()];
  },

  move: function() {
    this.chew();
    for (var i = 0; i < 2; i++) {
      this.position[i] += this.movingDirection[i];
    }
  },

  chew: function() {
    if (this.theta >= 30 || this.theta <= 0) {
      this.dTheta *= -1;
    }
    this.theta += this.dTheta;
    return this.theta;
  },

  draw: function(ctx) {
    RADIUS = 20;
    ctx.strokeStyle = "#FF0000";
    ctx.fillStyle = "#FF0000";
    ctx.beginPath();
    ctx.arc(
      this.getCx(),
      this.getCy(),
      RADIUS,
      (this.getTheta() * Math.PI) / 180,
      ((360 - this.getTheta()) * Math.PI) / 180
    );
    ctx.lineTo(this.getCx(), this.getCy());
    ctx.lineTo(
      this.getCx() + RADIUS * Math.cos((this.getTheta() * Math.PI) / 180),
      this.position[1] + RADIUS * Math.sin((this.getTheta() * Math.PI) / 180)
    );
    ctx.fill();
  }
};
