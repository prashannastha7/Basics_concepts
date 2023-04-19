//use during real time

import { EventEmitter } from 'node:events';

class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();
myEmitter.on('WaterFull', () => {
  console.log('Please turn off the motor !');
  setTimeout(() => {
    console.log("Please turn off the motor! Gentle reminder")
  }, 3000);
});

console.log("Script is running")
myEmitter.emit('WaterFull');
console.log("Script is still running")