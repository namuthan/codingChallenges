function Box(x, y, z, r) {
  this.pos = createVector(x, y, z);
  this.r = r;

  this.show = function() {
    push();
    translate(this.pos.x, this.pos.y, this.pos.z);
    noStroke();
    fill(255, 0, 0, 100);
    box(this.r);
    pop();
  };

  this.generate = function(level = 0) {
    var boxes = [];

    for (var x = -1; x < 2; x++) {
      for (var y = -1; y < 2; y++) {
        for (var z = -1; z < 2; z++) {
          let sum = abs(x) + abs(y) + abs(z);
          if (sum > 1) {
            let newR = this.r / 3;
            let newX = this.pos.x + x * newR;
            let newY = this.pos.y + y * newR;
            let newZ = this.pos.z + z * newR;

            let b = new Box(newX, newY, newZ, newR);
            boxes.push(b);
          }
        }
      }
    }
    return boxes;
  };
}
