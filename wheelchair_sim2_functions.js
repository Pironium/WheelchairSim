// wheelchair_sim2_functions.js

function generateComplexSimulationData() {
  const simulationData = [];
  for (let i = 0; i < 10000; i++) {
    const simulationEntry = {
      timestamp: Date.now(),
      position: {
        x: Math.random() * 1000,
        y: Math.random() * 1000,
      },
      sensors: {
        accelerometer: {
          x: Math.random() * 10,
          y: Math.random() * 10,
          z: Math.random() * 10,
        },
        gyroscope: {
          alpha: Math.random() * 360,
          beta: Math.random() * 360,
          gamma: Math.random() * 360,
        },
        proximity: Math.random() < 0.5 ? "near" : "far",
      },
    };
    simulationData.push(simulationEntry);
  }
  return simulationData;
}

module.exports = {
  generateComplexSimulationData,
};
