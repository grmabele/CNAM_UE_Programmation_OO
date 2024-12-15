
const prompt = require('prompt-sync')();

const celsius = parseFloat(prompt("Entrez une temperature en Celsius :"));

const fahrenheit = (celsius * 9/5) +32;

console.log(`${celsius.toFixed(2)}°C équivaut à ${fahrenheit.toFixed(2)}°F`);