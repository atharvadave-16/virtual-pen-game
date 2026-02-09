const canvas = document.getElementById("board");
const ctx = canvas.getContext("2d");
const brushSizeInput = document.getElementById("brushSize");
ctx.lineWidth = brushSizeInput.value;
ctx.lineCap = "round";
let strokes = [];
let currentStroke = [];



let isDrawing = false;

canvas.addEventListener("mousedown", (e) => {
  isDrawing = true;
  currentStroke = [];

  ctx.beginPath();
  ctx.moveTo(e.offsetX, e.offsetY);

  currentStroke.push({ x: e.offsetX, y: e.offsetY });
});


canvas.addEventListener("mousemove", (e) => {
  if (!isDrawing) return;

  ctx.lineTo(e.offsetX, e.offsetY);
  ctx.stroke();

  currentStroke.push({ x: e.offsetX, y: e.offsetY });
});


canvas.addEventListener("mouseup", () => {
  if (isDrawing && currentStroke.length > 0) {
    strokes.push(currentStroke);
  }
  isDrawing = false;
});


document.getElementById("clearBtn").addEventListener("click", () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  strokes = [];
});

document.getElementById("clearCanvasBtn").addEventListener("click", () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
});


brushSizeInput.addEventListener("input", () => {
  ctx.lineWidth = brushSizeInput.value;
});
document.getElementById("exportBtn").addEventListener("click", () => {
  const data = JSON.stringify(strokes, null, 2);

  const blob = new Blob([data], { type: "application/json" });
  const url = URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = "strokes.json";
  a.click();

  URL.revokeObjectURL(url);
});
document.getElementById("replayBtn").addEventListener("click", async () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (const stroke of strokes) {
    ctx.beginPath();
    ctx.moveTo(stroke[0].x, stroke[0].y);

    for (let i = 1; i < stroke.length; i++) {
      ctx.lineTo(stroke[i].x, stroke[i].y);
      ctx.stroke();
      await sleep(10);
    }
  }
});

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

