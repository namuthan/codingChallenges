var a = 0;

var sponge = [];
var _box;

function setup() {
  createCanvas(400, 400, WEBGL);
  _box = new Box(0, 0, 0, 200);
  sponge.push(_box);
}

function mousePressed() {
  console.log("mouse pressed");
  let newBoxes = [];
  for (index in sponge) {
    let generatdBoxs = sponge[index].generate();
    for (n in generatdBoxs) {
      newBoxes.push(generatdBoxs[n]);
    }
  }
  sponge = newBoxes;
}

function draw() {
  background(51);
  stroke(255);
  noFill();
  rotateX(a);
  rotateY(a * 0.4);
  rotateZ(a * 0.1);
  ambientLight(50);
  directionalLight(255, 0, 0, 0.25, 0.25, 0);
  pointLight(0, 0, 255, 0, 0, 0);

  for (b in sponge) {
    sponge[b].show();
  }
  a += 0.01;
}
