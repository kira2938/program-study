var Akabei = function(radius, speed, color, pacman, map, row, col) {
  Character.call(this, speed, map, row, col);
  this.radius = radius;
  this.color = color;
  this.pacman = pacman;
};

inheritFromCharacter(Akabei);

Akabei.prototype.getRadius = function () {
  return this.radius;
};

Akabei.prototype.getLeft = function () {
  return this.getCx() - this.getRadius();
};

Akabei.prototype.getTop = function () {
  return this.getCy() - this.getRadius();
};

Akabei.prototype.getRight = function () {
  return this.getCx() + this.getRadius();
};

Akabei.prototype.getBottom = function () {
  return this.getCy() + this.getRadius();
};

Akabei.prototype.decideDirection = function (duration) {
  if (Math.random() < 0.5) {
    if (this.pacman.getCx() - this.getCx() < 0) {
      this.nextMovingDirection.x = -1;
    } else {
      this.nextMovingDirection.x = 1;
    }
    this.nextMovingDirection.y = 0;
  } else {
    this.nextMovingDirection.x = 0;
    if (this.pacman.getCy() - this.getCy() < 0) {
      this.nextMovingDirection.y = -1;
    } else {
      this.nextMovingDirection.y = 1;
    }
  }
};

Akabei.prototype.move = function (duration) {
  this.decideDirection(duration);
  Character.prototype.move.call(this, duration);
};

Akabei.prototype.killPacman = function () {
  if (this.getDistance(this.pacman) <= Math.max(this.radius, this.pacman.radius)) {
    this.pacman.die();
  }
};


  // getCy: function() {
  //   return this.position[1];
  // },

  // getSpeed: function() {
  //   return this.speed;
  // },

  // move: function(pacman) {
  //   this.movingDirection[0] = this.movingDirection[1] = 0;
  //   var i = Math.floor(2 * Math.random());
  //   if (pacman.getPosition(i) - this.position[i] != 0) {
  //     this.movingDirection[i] =
  //       (pacman.getPosition(i) - this.position[i]) /
  //       Math.abs(pacman.getPosition(i) - this.position[i]);
  //     this.position[i] += this.getSpeed() * this.movingDirection[i];
  //   }
  // },

Akabei.prototype.draw = function(ctx) {
  var cx = this.getCx();
  var cy = this.getCy();
  var radius = this.radius();
  var bodyHeight =radius;
  var legHeight = radius / 5 * 2;
  ctx.fillStyle = this.color;
  ctx.beginPath();
  ctx.moveTo(cx - radius, cy);
  ctx.arc(cx, cy, radius, Math.PI, 2 * Math.PI);
  ctx.lineTo(cx + radius, cy + bodyHeight);
  ctx.lineTo(cx + radius / 3 * 2, cy + bodyHeight - legHeight);
  ctx.lineTo(cx + radius / 3, cy + bodyHeight);
  ctx.lineTo(cx, cy + bodyHeight - legHeight);
  ctx.lineTo(cx + radius / 3, cy + bodyHeight);
  ctx.lineTo(cx - radius / 3 * 2, cy + bodyHeight - legHeight);
  ctx.lineTo(cx - radius, cy + bodyHeight);
  ctx.lineTo(cx - radius, cy);
  ctx.fill();
    // ctx.stroke();
  ctx.fillStyle = "#FFFFFF";
  var leftEyeX = cx - 20 * radius / 50;
  var leftEyeY = cy - 4 * radius / 50;
  var rightEyeX = cx + 20 * radius / 50;
  var rightEyeY = cy + 4 * radius / 50;
  ctx.beginPath();
  ctx.arc(leftEyeX, leftEyeY, 16 * radius / 50, 0, Math.PI * 2);
  ctx.arc(rightEyeX, rightEyeY, 16 * radius / 50, 0, Math.PI * 2);
  ctx.fill();
  ctx.fillStyle = "#0000FF";
  ctx.beginPath();
  ctx.arc(leftEyeX - 8 * radius / 50, leftEyeY - 4 * radius / 50, 7 * radius / 50, 0, Math.PI * 2);
  ctx.arc(rightEyeX - 8 * radius / 50, rightEyeY - 4 * radius / 50, 7 * radius / 50, 0, Math.PI * 2);
  ctx.fill();
};
