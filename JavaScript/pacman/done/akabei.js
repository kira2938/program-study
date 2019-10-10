var Akabei = function(cx, cy, speed) {
  this.position = [cx, cy];
  this.movingDirection = [0, 0];
  this.speed = speed;
};

Akabei.prototype = {
  getCx: function() {
    return this.position[0];
  },

  getCy: function() {
    return this.position[1];
  },

  getSpeed: function() {
    return this.speed;
  },

  move: function(pacman) {
    this.movingDirection[0] = this.movingDirection[1] = 0;
    var i = Math.floor(2 * Math.random());
    if (pacman.getPosition(i) - this.position[i] != 0) {
      this.movingDirection[i] =
        (pacman.getPosition(i) - this.position[i]) /
        Math.abs(pacman.getPosition(i) - this.position[i]);
      this.position[i] += this.getSpeed() * this.movingDirection[i];
    }
  },

  draw: function(ctx) {
    cx = this.getCx();
    cy = this.getCy();
    RADIUS = 20;
    BODY_H = RADIUS;
    LEG_H = (RADIUS / 5) * 2;
    ctx.fillStyle = "#FF0000";
    ctx.beginPath();
    ctx.moveTo(cx - RADIUS, cy);
    ctx.arc(cx, cy, RADIUS, Math.PI, 2 * Math.PI);
    ctx.lineTo(cx + RADIUS, cy + BODY_H);
    ctx.lineTo(cx + (RADIUS / 3) * 2, cy + BODY_H - LEG_H);
    ctx.lineTo(cx + RADIUS / 3, cy + BODY_H);
    ctx.lineTo(cx, cy + BODY_H - LEG_H);
    ctx.lineTo(cx + RADIUS / 3, cy + BODY_H);
    ctx.lineTo(cx - (RADIUS / 3) * 2, cy + BODY_H - LEG_H);
    ctx.lineTo(cx - RADIUS, cy + BODY_H);
    ctx.lineTo(cx - RADIUS, cy);
    ctx.fill();
    // ctx.stroke();
    ctx.fillStyle = "#FFFFFF";
    ctx.beginPath();
    ctx.arc(
      cx - (20 * RADIUS) / 50,
      cy - 4,
      (16 * RADIUS) / 50,
      0,
      Math.PI * 2
    );
    ctx.arc(
      cx + (20 * RADIUS) / 50,
      cy - 4,
      (16 * RADIUS) / 50,
      0,
      Math.PI * 2
    );
    ctx.fill();
    ctx.fillStyle = "#0000FF";
    ctx.beginPath();
    ctx.arc(
      cx + ((-20 - 8) * RADIUS) / 50,
      cy - (4 * RADIUS) / 50,
      (7 * RADIUS) / 50,
      0,
      Math.PI * 2
    );
    ctx.arc(
      cx + ((20 - 8) * RADIUS) / 50,
      cy - (4 * RADIUS) / 50,
      (7 * RADIUS) / 50,
      0,
      Math.PI * 2
    );
    ctx.fill();
  }
};
