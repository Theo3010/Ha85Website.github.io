const boxs = Array.from(document.querySelectorAll('.background__box'));

function CalcBoxTotalWidth(box) {
  const boxIndex = boxs.indexOf(box);
  
  if (boxIndex === 0 || boxIndex === 10) return box.getBoundingClientRect().width * 1.5;
  
  return box.getBoundingClientRect().width * 2;
}

function CalcBoxOffsetX(box) {
  if (boxs.indexOf(box) === 0) return [0, box.getBoundingClientRect().width * 1.5];
  
  const boxIndex = boxs.indexOf(box);
  const boxOffset = box.getBoundingClientRect().width * (0.5 + boxIndex - 1);

  return boxOffset;
}

function CalcPercentXY(e, box) {
  const percentHeight = e.clientY / box.getBoundingClientRect().height * 100 - 4;
  const percentWidth = ((e.clientX - CalcBoxOffsetX(box)) / CalcBoxTotalWidth(box)) * 100;
  return [percentWidth, percentHeight];
}

function transforms(x, box) {
  const boxRect = box.getBoundingClientRect();
  const calcX = (x - boxRect.x - (boxRect.width / 2)) / 200;
  
  
  return "perspective(100px) "
       + "rotateY("+ calcX +"deg) ";
};

function radialGradient(e, box) {
  const x = CalcPercentXY(e, box)[0];
  const y = CalcPercentXY(e, box)[1];
  
  return "radial-gradient(circle at " + x + "% " + y + "%, " 
       + "rgba(200, 200, 200, .35) 10%, "
       + "rgba(200, 200, 200, 0) 40%) "
}


boxs.forEach(box => {
  box.onmousemove = (e) => {
    document.documentElement.style.setProperty("--background", radialGradient(e, box));
    document.documentElement.style.setProperty("--transform", transforms(e.clientX, box));
  };
});

