import { getLines } from '../../utils/index.js';

const lines = getLines(import.meta.url);

function solvePart1() {
  return lines;
}

console.time('Runtime');
console.log('Result Part 1:', solvePart1());
console.timeEnd('Runtime');
