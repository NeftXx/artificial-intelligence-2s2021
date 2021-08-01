const State = {
  DIRTY: "DIRTY",
  CLEAN: "CLEAN",
};

const Position = {
  RIGHT: "RIGHT",
  LEFT: "LEFT",
};

const locations = {
  A: { name: "A", state: State.DIRTY, position: Position.LEFT },
  B: { name: "B", state: State.DIRTY, position: Position.RIGHT },
};

const counters = [0, 0, 0, 0, 0, 0, 0, 0];

let locationVacuum = locations.A;
let stateCurrent = -1;

const $log = document.getElementById("log");
const $counters = document.getElementById("counters");
const $locationA = document.getElementById("locationA");
const $locationB = document.getElementById("locationB");

const $imgTrashA = document.createElement("img");
$imgTrashA.src = "./trash.png";
$imgTrashA.width = 95;
$imgTrashA.height = 65;

const $imgVacuum = document.createElement("img");
$imgVacuum.src = "./vacuum.png";
$imgVacuum.width = 175;
$imgVacuum.height = 125;

const $imgTrashB = $imgTrashA.cloneNode();

const intervalTest = setInterval(() => {
  test();
}, 2000);
const intervalDirty = setInterval(() => {
  randomDirty();
}, 6000);

const draw = () => {
  if (locations.A.state === State.DIRTY) {
    if (!$locationA.contains($imgTrashA)) {
      $locationA.appendChild($imgTrashA);
    }
  } else {
    if ($locationA.contains($imgTrashA)) {
      $locationA.removeChild($imgTrashA);
    }
  }

  if (locations.B.state === State.DIRTY) {
    if (!$locationB.contains($imgTrashB)) {
      $locationB.appendChild($imgTrashB);
    }
  } else {
    if ($locationB.contains($imgTrashB)) {
      $locationB.removeChild($imgTrashB);
    }
  }

  if (locationVacuum === locations.A) {
    if ($locationB.contains($imgVacuum)) {
      $locationB.removeChild($imgVacuum);
    }
    $locationA.appendChild($imgVacuum);
  } else {
    if ($locationA.contains($imgVacuum)) {
      $locationA.removeChild($imgVacuum);
    }
    $locationB.appendChild($imgVacuum);
  }
};

const randomDirty = () => {
  const values = Object.values(locations);
  values.forEach((location) => {
    const random = Math.random() < 0.55;
    if (random) {
      location.state = State.DIRTY;
    }
  })
};

const countStates = () => {
  const locationAIsDirty = locations.A.state === State.DIRTY;
  const locationBIsDirty = locations.B.state === State.DIRTY;
  const isLocationA = locationVacuum === locations.A;
  const isLocationB = locationVacuum === locations.B;

  if (locationAIsDirty && locationBIsDirty && isLocationA) {
    stateCurrent = 1;
    counters[0] = counters[0] + 1;
  } else if (locationAIsDirty && locationBIsDirty && isLocationB) {
    stateCurrent = 2;
    counters[1] = counters[1] + 1;
  } else if (locationAIsDirty && !locationBIsDirty && isLocationA) {
    stateCurrent = 3;
    counters[2] = counters[2] + 1;
  } else if (locationAIsDirty && !locationBIsDirty && isLocationB) {
    stateCurrent = 4;
    counters[3] = counters[3] + 1;
  } else if (!locationAIsDirty && locationBIsDirty && isLocationA) {
    stateCurrent = 5;
    counters[4] = counters[4] + 1;
  } else if (!locationAIsDirty && locationBIsDirty && isLocationB) {
    stateCurrent = 6;
    counters[5] = counters[5] + 1;
  } else if (!locationAIsDirty && !locationBIsDirty && isLocationA) {
    stateCurrent = 7;
    counters[6] = counters[6] + 1;
  } else if (!locationAIsDirty && !locationBIsDirty && isLocationB) {
    stateCurrent = 8;
    counters[7] = counters[7] + 1;
  }
};

const reflexAgent = () => {
  if (locationVacuum.state === State.DIRTY) {
    return (locationVacuum.state = State.CLEAN);
  }

  if (locationVacuum === locations.A) {
    locationVacuum = locations.B;
  } else if (locationVacuum === locations.B) {
    locationVacuum = locations.A;
  }

  return locationVacuum.position;
};

const test = () => {
  draw();
  countStates();
  const states = counters
  .map((count, index) => `<p><b>State No. ${index + 1}:</b> ${count}</p>`)
  .join("");
  $counters.innerHTML = `Current state: ${stateCurrent}<br /><h2>Counters</h2>${states}`;
  const actionResult = reflexAgent();
  $log.innerHTML += `<br />Location: ${locationVacuum.name}\t| Action: ${actionResult}\t| State: ${stateCurrent}`;
  const isMaximumCount = counters.every((count) => count >= 2);
  console.log(isMaximumCount);
  if (isMaximumCount) {
    clearInterval(intervalTest);
    clearInterval(intervalDirty);
  }
};
